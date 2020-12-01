Sendmode Input

!ESC::send,{Blind}{sc029}

; +CapsLock::CapsLock
; ; sc03A::send,{CapsLock up}{CapsLock down}
; ; +sc03A::send,{CapsLock up}{CapsLock down}
; CapsLock::Return

;;;DEFAULT;;;
>!s::send,{Left}
>!e::send,{Up}
>!d::send,{Down}
>!f::send,{Right}
>!u::send,{PrintScreen}
>!i::send,{ScrollLock}
>!o::send,{Pause}
>!k::send,{Home}
>!,::send,{End}
>!l::send,{PgUp}
>!.::send,{PgDn}
>!j::send,{Ins}
>!m::send,{Del}
>!1::send,{F1}
>!2::send,{F2}
>!3::send,{F3}
>!4::send,{F4}
>!5::send,{F5}
>!6::send,{F6}
>!7::send,{F7}
>!8::send,{F8}
>!9::send,{F9}
>!0::send,{F10}
>!-::send,{F11}
>!=::send,{F12}

;;;Ctrl;;;
<^>!s::send,{Ctrl down}{Left}{Ctrl up}
<^>!e::send,{Ctrl down}{Up}{Ctrl up}
<^>!d::send,{Ctrl down}{Down}{Ctrl up}
<^>!f::send,{Ctrl down}{Right}{Ctrl up}
<^>!u::send,{Ctrl down}{PrintScreen}{Ctrl up}
<^>!i::send,{Ctrl down}{ScrollLock}{Ctrl up}
<^>!o::send,{Ctrl down}{Pause}{Ctrl up}
<^>!k::send,{Ctrl down}{Home}{Ctrl up}
<^>!,::send,{Ctrl down}{End}{Ctrl up}
<^>!l::send,{Ctrl down}{PgUp}{Ctrl up}
<^>!.::send,{Ctrl down}{PgDn}{Ctrl up}
<^>!j::send,{Ctrl down}{Ins}{Ctrl up}
<^>!m::send,{Ctrl down}{Del}{Ctrl up}
<^>!1::send,{Ctrl down}{F1}{Ctrl up}
<^>!2::send,{Ctrl down}{F2}{Ctrl up}
<^>!3::send,{Ctrl down}{F3}{Ctrl up}
<^>!4::send,{Ctrl down}{F4}{Ctrl up}
<^>!5::send,{Ctrl down}{F5}{Ctrl up}
<^>!6::send,{Ctrl down}{F6}{Ctrl up}
<^>!7::send,{Ctrl down}{F7}{Ctrl up}
<^>!8::send,{Ctrl down}{F8}{Ctrl up}
<^>!9::send,{Ctrl down}{F9}{Ctrl up}
<^>!0::send,{Ctrl down}{F10}{Ctrl up}
<^>!-::send,{Ctrl down}{F11}{Ctrl up}
<^>!=::send,{Ctrl down}{F12}{Ctrl up}

;;;Shift;;;
+>!s::send,{Shift down}{Left}{Shift up}
+>!e::send,{Shift down}{Up}{Shift up}
+>!d::send,{Shift down}{Down}{Shift up}
+>!f::send,{Shift down}{Right}{Shift up}
+>!u::send,{Shift down}{PrintScreen}{Shift up}
+>!i::send,{Shift down}{ScrollLock}{Shift up}
+>!o::send,{Shift down}{Pause}{Shift up}
+>!k::send,{Shift down}{Home}{Shift up}
+>!,::send,{Shift down}{End}{Shift up}
+>!l::send,{Shift down}{PgUp}{Shift up}
+>!.::send,{Shift down}{PgDn}{Shift up}
+>!j::send,{Shift down}{Ins}{Shift up}
+>!m::send,{Shift down}{Del}{Shift up}
+>!1::send,{Shift down}{F1}{Shift up}
+>!2::send,{Shift down}{F2}{Shift up}
+>!3::send,{Shift down}{F3}{Shift up}
+>!4::send,{Shift down}{F4}{Shift up}
+>!5::send,{Shift down}{F5}{Shift up}
+>!6::send,{Shift down}{F6}{Shift up}
+>!7::send,{Shift down}{F7}{Shift up}
+>!8::send,{Shift down}{F8}{Shift up}
+>!9::send,{Shift down}{F9}{Shift up}
+>!0::send,{Shift down}{F10}{Shift up}
+>!-::send,{Shift down}{F11}{Shift up}
+>!=::send,{Shift down}{F12}{Shift up}

;;;Alt;;;
<!>!s::send,{Alt down}{Left}{Alt up}
<!>!e::send,{Alt down}{Up}{Alt up}
<!>!d::send,{Alt down}{Down}{Alt up}
<!>!f::send,{Alt down}{Right}{Alt up}
<!>!u::send,{Alt down}{PrintScreen}{Alt up}
<!>!i::send,{Alt down}{ScrollLock}{Alt up}
<!>!o::send,{Alt down}{Pause}{Alt up}
<!>!k::send,{Alt down}{Home}{Alt up}
<!>!,::send,{Alt down}{End}{Alt up}
<!>!l::send,{Alt down}{PgUp}{Alt up}
<!>!.::send,{Alt down}{PgDn}{Alt up}
<!>!j::send,{Alt down}{Ins}{Alt up}
<!>!m::send,{Alt down}{Del}{Alt up}
<!>!1::send,{Alt down}{F1}{Alt up}
<!>!2::send,{Alt down}{F2}{Alt up}
<!>!3::send,{Alt down}{F3}{Alt up}
<!>!4::send,{Alt down}{F4}{Alt up}
<!>!5::send,{Alt down}{F5}{Alt up}
<!>!6::send,{Alt down}{F6}{Alt up}
<!>!7::send,{Alt down}{F7}{Alt up}
<!>!8::send,{Alt down}{F8}{Alt up}
<!>!9::send,{Alt down}{F9}{Alt up}
<!>!0::send,{Alt down}{F10}{Alt up}
<!>!-::send,{Alt down}{F11}{Alt up}
<!>!=::send,{Alt down}{F12}{Alt up}

;;;LWin;;;
<#>!s::send,{LWin down}{Left}{LWin up}
<#>!e::send,{LWin down}{Up}{LWin up}
<#>!d::send,{LWin down}{Down}{LWin up}
<#>!f::send,{LWin down}{Right}{LWin up}
<#>!u::send,{LWin down}{PrintScreen}{LWin up}
<#>!i::send,{LWin down}{ScrollLock}{LWin up}
<#>!o::send,{LWin down}{Pause}{LWin up}
<#>!k::send,{LWin down}{Home}{LWin up}
<#>!,::send,{LWin down}{End}{LWin up}
<#>!l::send,{LWin down}{PgUp}{LWin up}
<#>!j::send,{LWin down}{Ins}{LWin up}
<#>!m::send,{Lwin down}{Del}{Lwin up}
<#>!1::send,{LWin down}{F1}{LWin up}
<#>!2::send,{LWin down}{F2}{LWin up}
<#>!3::send,{LWin down}{F3}{LWin up}
<#>!4::send,{LWin down}{F4}{LWin up}
<#>!5::send,{LWin down}{F5}{LWin up}
<#>!6::send,{LWin down}{F6}{LWin up}
<#>!7::send,{LWin down}{F7}{LWin up}
<#>!8::send,{LWin down}{F8}{LWin up}
<#>!9::send,{LWin down}{F9}{LWin up}
<#>!0::send,{LWin down}{F10}{LWin up}
<#>!-::send,{LWin down}{F11}{LWin up}
<#>!=::send,{LWin down}{F12}{LWin up}

;;;Ctrl Shift;;;
^+>!s::send,{Ctrl down}{Shift down}{Left}{Shift up}{Ctrl up}
^+>!e::send,{Ctrl down}{Shift down}{Up}{Shift up}{Ctrl up}
^+>!d::send,{Ctrl down}{Shift down}{Down}{Shift up}{Ctrl up}
^+>!f::send,{Ctrl down}{Shift down}{Right}{Shift up}{Ctrl up}
^+>!u::send,{Ctrl down}{Shift down}{PrintScreen}{Shift up}{Ctrl up}
^+>!i::send,{Ctrl down}{Shift down}{ScrollLock}{Shift up}{Ctrl up}
^+>!o::send,{Ctrl down}{Shift down}{Pause}{Shift up}{Ctrl up}
^+>!k::send,{Ctrl down}{Shift down}{Home}{Shift up}{Ctrl up}
^+>!,::send,{Ctrl down}{Shift down}{End}{Shift up}{Ctrl up}
^+>!l::send,{Ctrl down}{Shift down}{PgUp}{Shift up}{Ctrl up}
^+>!.::send,{Ctrl down}{Shift down}{PgDn}{Shift up}{Ctrl up}
^+>!j::send,{Ctrl down}{Shift down}{Ins}{Shift up}{Ctrl up}
^+>!m::send,{Ctrl down}{Shift down}{Del}{Shift up}{Ctrl up}
^+>!1::send,{Ctrl down}{Shift down}{F1}{Shift up}{Ctrl up}
^+>!2::send,{Ctrl down}{Shift down}{F2}{Shift up}{Ctrl up}
^+>!3::send,{Ctrl down}{Shift down}{F3}{Shift up}{Ctrl up}
^+>!4::send,{Ctrl down}{Shift down}{F4}{Shift up}{Ctrl up}
^+>!5::send,{Ctrl down}{Shift down}{F5}{Shift up}{Ctrl up}
^+>!6::send,{Ctrl down}{Shift down}{F6}{Shift up}{Ctrl up}
^+>!7::send,{Ctrl down}{Shift down}{F7}{Shift up}{Ctrl up}
^+>!8::send,{Ctrl down}{Shift down}{F8}{Shift up}{Ctrl up}
^+>!9::send,{Ctrl down}{Shift down}{F9}{Shift up}{Ctrl up}
^+>!0::send,{Ctrl down}{Shift down}{F10}{Shift up}{Ctrl up}
^+>!-::send,{Ctrl down}{Shift down}{F11}{Shift up}{Ctrl up}
^+>!=::send,{Ctrl down}{Shift down}{F12}{Shift up}{Ctrl up}

;;;Shift Alt;;;
^<!>!s::send,{Shift down}{Alt down}{Left}{Alt up}{Shift up}
^<!>!e::send,{Shift down}{Alt down}{Up}{Alt up}{Shift up}
^<!>!d::send,{Shift down}{Alt down}{Down}{Alt up}{Shift up}
^<!>!f::send,{Shift down}{Alt down}{Right}{Alt up}{Shift up}
^<!>!u::send,{Shift down}{Alt down}{PrintScreen}{Alt up}{Shift up}
^<!>!i::send,{Shift down}{Alt down}{ScrollLock}{Alt up}{Shift up}
^<!>!o::send,{Shift down}{Alt down}{Pause}{Alt up}{Shift up}
^<!>!k::send,{Shift down}{Alt down}{Home}{Alt up}{Shift up}
^<!>!,::send,{Shift down}{Alt down}{End}{Alt up}{Shift up}
^<!>!l::send,{Shift down}{Alt down}{PgUp}{Alt up}{Shift up}
^<!>!.::send,{Shift down}{Alt down}{PgDn}{Alt up}{Shift up}
^<!>!j::send,{Shift down}{Alt down}{Ins}{Alt up}{Shift up}
^<!>!m::send,{Shift down}{Alt down}{Del}{Alt up}{Shift up}
^<!>!1::send,{Shift down}{Alt down}{F1}{Alt up}{Shift up}
^<!>!2::send,{Shift down}{Alt down}{F2}{Alt up}{Shift up}
^<!>!3::send,{Shift down}{Alt down}{F3}{Alt up}{Shift up}
^<!>!4::send,{Shift down}{Alt down}{F4}{Alt up}{Shift up}
^<!>!5::send,{Shift down}{Alt down}{F5}{Alt up}{Shift up}
^<!>!6::send,{Shift down}{Alt down}{F6}{Alt up}{Shift up}
^<!>!7::send,{Shift down}{Alt down}{F7}{Alt up}{Shift up}
^<!>!8::send,{Shift down}{Alt down}{F8}{Alt up}{Shift up}
^<!>!9::send,{Shift down}{Alt down}{F9}{Alt up}{Shift up}
^<!>!0::send,{Shift down}{Alt down}{F10}{Alt up}{Shift up}
^<!>!-::send,{Shift down}{Alt down}{F11}{Alt up}{Shift up}
^<!>!=::send,{Shift down}{Alt down}{F12}{Alt up}{Shift up}

;;;Ctrl Alt;;;
+<!>!s::send,{Ctrl down}{Alt down}{Left}{Alt up}{Ctrl up}
+<!>!e::send,{Ctrl down}{Alt down}{Up}{Alt up}{Ctrl up}
+<!>!d::send,{Ctrl down}{Alt down}{Down}{Alt up}{Ctrl up}
+<!>!f::send,{Ctrl down}{Alt down}{Right}{Alt up}{Ctrl up}
+<!>!u::send,{Ctrl down}{Alt down}{PrintScreen}{Alt up}{Ctrl up}
+<!>!i::send,{Ctrl down}{Alt down}{ScrollLock}{Alt up}{Ctrl up}
+<!>!o::send,{Ctrl down}{Alt down}{Pause}{Alt up}{Ctrl up}
+<!>!k::send,{Ctrl down}{Alt down}{Home}{Alt up}{Ctrl up}
+<!>!,::send,{Ctrl down}{Alt down}{End}{Alt up}{Ctrl up}
+<!>!l::send,{Ctrl down}{Alt down}{PgUp}{Alt up}{Ctrl up}
+<!>!.::send,{Ctrl down}{Alt down}{PgDn}{Alt up}{Ctrl up}
+<!>!j::send,{Ctrl down}{Alt down}{Ins}{Alt up}{Ctrl up}
+<!>!m::send,{Ctrl down}{Alt down}{Del}{Alt up}{Ctrl up}
+<!>!1::send,{Ctrl down}{Alt down}{F1}{Alt up}{Ctrl up}
+<!>!2::send,{Ctrl down}{Alt down}{F2}{Alt up}{Ctrl up}
+<!>!3::send,{Ctrl down}{Alt down}{F3}{Alt up}{Ctrl up}
+<!>!4::send,{Ctrl down}{Alt down}{F4}{Alt up}{Ctrl up}
+<!>!5::send,{Ctrl down}{Alt down}{F5}{Alt up}{Ctrl up}
+<!>!6::send,{Ctrl down}{Alt down}{F6}{Alt up}{Ctrl up}
+<!>!7::send,{Ctrl down}{Alt down}{F7}{Alt up}{Ctrl up}
+<!>!8::send,{Ctrl down}{Alt down}{F8}{Alt up}{Ctrl up}
+<!>!9::send,{Ctrl down}{Alt down}{F9}{Alt up}{Ctrl up}
+<!>!0::send,{Ctrl down}{Alt down}{F10}{Alt up}{Ctrl up}
+<!>!-::send,{Ctrl down}{Alt down}{F11}{Alt up}{Ctrl up}
+<!>!=::send,{Ctrl down}{Alt down}{F12}{Alt up}{Ctrl up}

;;;Shift LWin;;;
^#>!s::send,{Shift down}{LWin down}{Left}{LWin up}{Shift up}
^#>!e::send,{Shift down}{LWin down}{Up}{LWin up}{Shift up}
^#>!d::send,{Shift down}{LWin down}{Down}{LWin up}{Shift up}
^#>!f::send,{Shift down}{LWin down}{Right}{LWin up}{Shift up}
^#>!u::send,{Shift down}{LWin down}{PrintScreen}{LWin up}{Shift up}
^#>!i::send,{Shift down}{LWin down}{ScrollLock}{LWin up}{Shift up}
^#>!o::send,{Shift down}{LWin down}{Pause}{LWin up}{Shift up}
^#>!k::send,{Shift down}{LWin down}{Home}{LWin up}{Shift up}
^#>!,::send,{Shift down}{LWin down}{End}{LWin up}{Shift up}
^#>!l::send,{Shift down}{LWin down}{PgUp}{LWin up}{Shift up}
^#>!.::send,{Shift down}{LWin down}{PgDn}{LWin up}{Shift up}
^#>!j::send,{Shift down}{LWin down}{Ins}{LWin up}{Shift up}
^#>!m::send,{Shift down}{LWin down}{Del}{LWin up}{Shift up}
^#>!1::send,{Shift down}{LWin down}{F1}{LWin up}{Shift up}
^#>!2::send,{Shift down}{LWin down}{F2}{LWin up}{Shift up}
^#>!3::send,{Shift down}{LWin down}{F3}{LWin up}{Shift up}
^#>!4::send,{Shift down}{LWin down}{F4}{LWin up}{Shift up}
^#>!5::send,{Shift down}{LWin down}{F5}{LWin up}{Shift up}
^#>!6::send,{Shift down}{LWin down}{F6}{LWin up}{Shift up}
^#>!7::send,{Shift down}{LWin down}{F7}{LWin up}{Shift up}
^#>!8::send,{Shift down}{LWin down}{F8}{LWin up}{Shift up}
^#>!9::send,{Shift down}{LWin down}{F9}{LWin up}{Shift up}
^#>!0::send,{Shift down}{LWin down}{F10}{LWin up}{Shift up}
^#>!-::send,{Shift down}{LWin down}{F11}{LWin up}{Shift up}
^#>!=::send,{Shift down}{LWin down}{F12}{LWin up}{Shift up}

RAlt::return



;;;MOUSE;;;
CapsLock::
keywait, CapsLock, U
keywait, CapsLock, D T0.2
if (ErrorLevel = 1) {
	return ;If CAPSLOCK is pressed once, do nothing
}
else {　;pressed twice within 0.2 seconds
	if (mousemode) {
		mousemode := False　;turn off the mousemode
		return
	}
	else{
		mousemode := True ;turn off the mousemode
		return
	}
}
return

#if GetKeyState("CapsLock", "P") or (mousemode)
;;;MOVE;;;
	w::
	MouseMove 0,-20,0,R
	return
	s::
	MouseMove 0,20,0,R
	return
	a::
	MouseMove -20,0,0,R
	return
	d::
	MouseMove 20,0,0,R
	return
	<!w::
	MouseMove 0,-10,0,R
	return
	<!s::
	MouseMove 0,10,0,R
	return
	<!a::
	MouseMove -10,0,0,R
	return
	<!d::
	MouseMove 10,0,0,R
	return
;;;SCROLL;;;
	r::
	Click,WU,1
	return
	f::
	Click,WD,1
	return
	q::
	ControlGetFocus, fcontrol, A
	Loop 2 ; <-- scroll speed
	SendMessage, 0x114, 0, 0, %fcontrol%, A ; 0x114: WM_HSCROLL, 0: SB_LINERIGHT.
	return
	e::
	ControlGetFocus, fcontrol, A
	Loop 2 ; <-- scroll speed.
	SendMessage, 0x114, 1, 0, %fcontrol%, A ; 0x114: WM_HSCROLL, 1: SB_LINELEFT.
	return
;;;CLICK;;;
	Space::
	send,{Lbutton}
	return
	c::
	send,{Mbutton}
	return
	x::
	send,{Rbutton}
	return
	
	;;;ALTER CAPSLOCK;;;
	Enter::
	KeyWait,CapsLock
	KeyWait,Enter
	if GetKeyState("CapsLock","T"){
		SetCapslockState, Off
		return
	}
	else{
		SetCapslockState, On
		return
	}
	return
#if




;;;CONTROL IME;;;
; 左Shiftが単体で押されたら、直接入力
~LShift Up::
if (A_PriorKey = "LShift") {
    Send, {vkF2sc070B}{vkF3sc029}
}
Return

; 右Shiftが単体で押されたら、ひらがな入力
~RShift Up::
if (A_PriorKey = "RShift") {
    Send, {vkF2sc070B}
}
Return

;;;CONTROL THIS SCRIPT;;;
>^r::
msgbox,Reloaded
Reload
Return

