"""imagehashを使用して重複画像を削除する"""

import argparse
import logging
import os
import shutil
from collections import defaultdict

import imagehash
import tqdm
from PIL import Image

logger = logging.getLogger(__name__)
logfile = os.path.join(os.path.dirname(__file__), 'remove_duplicated_image.log')
logging.basicConfig(level=logging.INFO)
handler = logging.FileHandler(logfile)
handler.setLevel(logging.INFO)
logger.addHandler(handler)


def make_imagehashes(path: str) -> dict:
    """画像のパスを受け取り、imagehashを返す
    path内の画像をimagehashで比較し、重複画像を削除する

    Args:
        path (str): 画像のパス

    Returns:
        imagehashes (dict[List]): imagehashの情報{hash: [path1, path2, ...]}

    """
    if os.path.split(path)[-1] == 'duplicated':
        return None, 0
    imagehashes = defaultdict(list)
    duplicated = 0
    for file in tqdm.tqdm(os.listdir(path)):
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            try:
                image = Image.open(os.path.join(path, file))
                hash = str(imagehash.average_hash(image))
                if hash not in imagehashes:
                    imagehashes[hash].append(os.path.join(path, file))
                else:
                    logger.debug(f'Duplicated image: {os.path.join(path, file)}')
                    duplicated += 1
                    imagehashes[hash].append(os.path.join(path, file))
            except OSError:
                logger.info(f'Failed to open {os.path.join(path, file)}')
  
    return imagehashes, duplicated


def remove_duplicated_images(imagehashes: dict, path: str):
    """重複画像を削除する
    
    Args:
        imagehashes (dict[List]): imagehashの情報{hash: [path1, path2, ...]}
        path (str): 画像のパス

    Returns:
        None
    """
    dup_hashes = [h for h in imagehashes if len(imagehashes[h]) > 1]
    for hash in dup_hashes:
        # if len(imagehashes[hash]) > 2:
        #     print(hash)
        for dup_file in imagehashes[hash][1:]:
            os.remove(dup_file)


def debug_check_duplicated_images(imagehashes: dict, path: str):
    """デバッグ用関数(重複画像を削除せず別フォルダへコピーする))

    Args:
        imagehashes (dict[List]): imagehashの情報{hash: [path1, path2, ...]}
        path (str): 画像のパス

    Returns:
        None
    """
    subdir = os.path.join(path, 'duplicated')
    os.makedirs(subdir, exist_ok=True)

    dup_hashes = [h for h in imagehashes if len(imagehashes[h]) > 1]
    for hash in dup_hashes:
        for idx, file in enumerate(imagehashes[hash]):
            shutil.copy(file, os.path.join(subdir, f'{hash}_{idx:02}_{os.path.basename(file)}'))


def main():
    """メイン関数"""
    parser = argparse.ArgumentParser(description='Remove duplicated images.')
    parser.add_argument('root_dir', help='Path to image files.')
    parser.add_argument('--debug', help='Debug mode(just copy to subdir)', default=False, action='store_true')
    args = parser.parse_args()
    for root, dirs, files in os.walk(args.root_dir):
        imagehashes, dup_count = make_imagehashes(root)
        logger.info(f'{dup_count} duplicated images were found in {root}')
        if dup_count > 0:
            if args.debug:
                debug_check_duplicated_images(imagehashes, root)
            else:
                remove_duplicated_images(imagehashes, root)

if __name__ == '__main__':
    main()