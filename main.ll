; ModuleID = "meu_modulo"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"a" = alloca i32
  store i32 1, i32* %"a"
  %"b" = alloca i32
  store i32 12, i32* %"b"
  %".4" = load i32, i32* %"a"
  %".5" = load i32, i32* %"b"
  %"_t0" = add i32 %".4", %".5"
  %"_t0.1" = alloca i32
  store i32 %"_t0", i32* %"_t0.1"
  %".7" = load i32, i32* %"b"
  %"_t1" = sub i32 %".7", 1
  %"_t1.1" = alloca i32
  store i32 %"_t1", i32* %"_t1.1"
  %".9" = load i32, i32* %"_t0.1"
  %".10" = load i32, i32* %"_t1.1"
  %"_t2" = sdiv i32 %".9", %".10"
  %"_t2.1" = alloca i32
  store i32 %"_t2", i32* %"_t2.1"
  %".12" = load i32, i32* %"_t2.1"
  %".13" = load i32, i32* %"a"
  %"_t3" = mul i32 %".12", %".13"
  %"_t3.1" = alloca i32
  store i32 %"_t3", i32* %"_t3.1"
  %".15" = load i32, i32* %"a"
  %".16" = load i32, i32* %"b"
  %"_t4" = sdiv i32 %".15", %".16"
  %"_t4.1" = alloca i32
  store i32 %"_t4", i32* %"_t4.1"
  %".18" = load i32, i32* %"_t3.1"
  %".19" = load i32, i32* %"_t4.1"
  %"_t5" = sub i32 %".18", %".19"
  %"_t5.1" = alloca i32
  store i32 %"_t5", i32* %"_t5.1"
  %".21" = load i32, i32* %"_t5.1"
  %"c" = alloca i32
  store i32 %".21", i32* %"c"
  %".23" = bitcast [12 x i8]* @"str0" to i8*
  %".24" = call i32 (i8*, ...) @"printf"(i8* %".23")
  %"tmp_c" = load i32, i32* %"c"
  %".25" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".26" = call i32 (i8*, ...) @"printf"(i8* %".25", i32 %"tmp_c")
  ret i32 0
}

declare i32 @"printf"(i8* %".1", ...)

@"str0" = internal constant [12 x i8] c"resultado:\0a\00"
@"fmt_int" = internal constant [4 x i8] c"%d\0a\00"