; ModuleID = "meu_modulo"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"a" = alloca i32
  store i32 3, i32* %"a"
  %"b" = alloca i32
  store i32 4, i32* %"b"
  %"c" = alloca i32
  store i32 5, i32* %"c"
  %".5" = load i32, i32* %"a"
  %".6" = load i32, i32* %"b"
  %"_t0" = add i32 %".5", %".6"
  %"_t0.1" = alloca i32
  store i32 %"_t0", i32* %"_t0.1"
  %".8" = load i32, i32* %"_t0.1"
  %".9" = load i32, i32* %"c"
  %"cmptmp" = icmp sgt i32 %".8", %".9"
  %"bool_to_int" = zext i1 %"cmptmp" to i32
  %"_t1" = alloca i32
  store i32 %"bool_to_int", i32* %"_t1"
  %".11" = load i32, i32* %"a"
  %".12" = load i32, i32* %"c"
  %"_t2" = add i32 %".11", %".12"
  %"_t2.1" = alloca i32
  store i32 %"_t2", i32* %"_t2.1"
  %".14" = load i32, i32* %"_t2.1"
  %".15" = load i32, i32* %"b"
  %"cmptmp.1" = icmp sgt i32 %".14", %".15"
  %"bool_to_int.1" = zext i1 %"cmptmp.1" to i32
  %"_t3" = alloca i32
  store i32 %"bool_to_int.1", i32* %"_t3"
  %".17" = load i32, i32* %"_t1"
  %".18" = load i32, i32* %"_t3"
  %"andtmp" = and i32 %".17", %".18"
  %"_t4" = alloca i32
  store i32 %"andtmp", i32* %"_t4"
  %".20" = load i32, i32* %"b"
  %".21" = load i32, i32* %"c"
  %"_t5" = add i32 %".20", %".21"
  %"_t5.1" = alloca i32
  store i32 %"_t5", i32* %"_t5.1"
  %".23" = load i32, i32* %"_t5.1"
  %".24" = load i32, i32* %"a"
  %"cmptmp.2" = icmp sgt i32 %".23", %".24"
  %"bool_to_int.2" = zext i1 %"cmptmp.2" to i32
  %"_t6" = alloca i32
  store i32 %"bool_to_int.2", i32* %"_t6"
  %".26" = load i32, i32* %"_t4"
  %".27" = load i32, i32* %"_t6"
  %"andtmp.1" = and i32 %".26", %".27"
  %"_t7" = alloca i32
  store i32 %"andtmp.1", i32* %"_t7"
  %".29" = load i32, i32* %"_t7"
  %"ifcond" = icmp ne i32 %".29", 0
  br i1 %"ifcond", label %"L0", label %"cont_1"
L0:
  %".32" = load i32, i32* %"a"
  %".33" = load i32, i32* %"b"
  %"cmptmp.3" = icmp eq i32 %".32", %".33"
  %"bool_to_int.3" = zext i1 %"cmptmp.3" to i32
  %"_t8" = alloca i32
  store i32 %"bool_to_int.3", i32* %"_t8"
  %".35" = load i32, i32* %"b"
  %".36" = load i32, i32* %"c"
  %"cmptmp.4" = icmp eq i32 %".35", %".36"
  %"bool_to_int.4" = zext i1 %"cmptmp.4" to i32
  %"_t9" = alloca i32
  store i32 %"bool_to_int.4", i32* %"_t9"
  %".38" = load i32, i32* %"_t8"
  %".39" = load i32, i32* %"_t9"
  %"andtmp.2" = and i32 %".38", %".39"
  %"_t10" = alloca i32
  store i32 %"andtmp.2", i32* %"_t10"
  %".41" = load i32, i32* %"_t10"
  %"ifcond.1" = icmp ne i32 %".41", 0
  br i1 %"ifcond.1", label %"L3", label %"cont_3"
cont_1:
  br label %"L1"
L1:
  %".73" = bitcast [21 x i8]* @"str3" to i8*
  %".74" = call i32 (i8*, ...) @"printf"(i8* %".73")
  br label %"L2"
L3:
  %".44" = bitcast [22 x i8]* @"str0" to i8*
  %".45" = call i32 (i8*, ...) @"printf"(i8* %".44")
  br label %"L5"
cont_3:
  br label %"L4"
L4:
  br label %"L5"
L5:
  %".48" = load i32, i32* %"a"
  %".49" = load i32, i32* %"b"
  %"cmptmp.5" = icmp eq i32 %".48", %".49"
  %"bool_to_int.5" = zext i1 %"cmptmp.5" to i32
  %"_t11" = alloca i32
  store i32 %"bool_to_int.5", i32* %"_t11"
  %".51" = load i32, i32* %"a"
  %".52" = load i32, i32* %"c"
  %"cmptmp.6" = icmp eq i32 %".51", %".52"
  %"bool_to_int.6" = zext i1 %"cmptmp.6" to i32
  %"_t12" = alloca i32
  store i32 %"bool_to_int.6", i32* %"_t12"
  %".54" = load i32, i32* %"_t11"
  %".55" = load i32, i32* %"_t12"
  %"ortmp" = or i32 %".54", %".55"
  %"_t13" = alloca i32
  store i32 %"ortmp", i32* %"_t13"
  %".57" = load i32, i32* %"b"
  %".58" = load i32, i32* %"c"
  %"cmptmp.7" = icmp eq i32 %".57", %".58"
  %"bool_to_int.7" = zext i1 %"cmptmp.7" to i32
  %"_t14" = alloca i32
  store i32 %"bool_to_int.7", i32* %"_t14"
  %".60" = load i32, i32* %"_t13"
  %".61" = load i32, i32* %"_t14"
  %"ortmp.1" = or i32 %".60", %".61"
  %"_t15" = alloca i32
  store i32 %"ortmp.1", i32* %"_t15"
  %".63" = load i32, i32* %"_t15"
  %"ifcond.2" = icmp ne i32 %".63", 0
  br i1 %"ifcond.2", label %"L6", label %"cont_6"
L6:
  %".66" = bitcast [21 x i8]* @"str1" to i8*
  %".67" = call i32 (i8*, ...) @"printf"(i8* %".66")
  br label %"L8"
cont_6:
  br label %"L7"
L7:
  %".69" = bitcast [20 x i8]* @"str2" to i8*
  %".70" = call i32 (i8*, ...) @"printf"(i8* %".69")
  br label %"L8"
L8:
  br label %"L2"
L2:
  ret i32 0
}

declare i32 @"printf"(i8* %".1", ...)

@"str0" = internal constant [22 x i8] c"Triangulo Equilatero\0a\00"
@"str1" = internal constant [21 x i8] c"Triangulo Isosceles\0a\00"
@"str2" = internal constant [20 x i8] c"Trinagulo Escaleno\0a\00"
@"str3" = internal constant [21 x i8] c"Nao forma triangulo\0a\00"