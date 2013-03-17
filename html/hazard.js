

var paper = Raphael(document.getElementById("circuit"), 960, 650);

/********************************* PC *******************************/
var pc =paper.rect(150, 285, 20, 50);
paper.text(150+10, 285+25, "pc").attr({"font-size":"12px", "font-weight":"bold"});
var pc_to_read_addr = paper.path("M170, 310L200 310");
var pc_to_add = paper.path("M185 310L185 85L200 85");


/********************* Instruction Memory *********************/

var inst_memory = paper.rect(200, 300, 70, 100);
paper.text(235, 350, "Instruction\nMemory").attr({"font-size":"12px", "font-weight":"bold"});

var read_address = paper.text(205, 312, "Read\naddress").attr("text-anchor","start");
//var inst_to_all = paper.path("M270 350L280 350"); 
var op_to_control = paper.path("M280 350L280 200L370 200") 
var op = paper.text(285, 192, "Instruction[31:26]").attr("text-anchor","start");
var rs_to_read_reg1 = paper.path("M270 350L280 350L280 320L400 320");
var rs = paper.text(285, 312, "Instruction[25:21]").attr("text-anchor","start");
var rt_to_read_reg2 = paper.path("M280 350L400 350");
var rt = paper.text(285, 342, "Instruction[20:16]").attr("text-anchor","start");
var rt_to_mux1 = paper.path("M325 350L325 372L355 372");
var imm_to_sign_extent = paper.path("M280 350L280 530L430 530");
var imm = paper.text(285, 540, "Instruction[15:0]").attr("text-anchor","start");
var rd_to_mux1 = paper.path("M270 350L280 350L280 407L355 407");
var rd = paper.text(285, 430, "Instruction[15:11]").attr("text-anchor","start");
var funct_to_alu_control = paper.path("M400 530L400 550L555 550").attr("stroke-dasharray", "-");


/************************  mux1 ***************************/
var mux1 =paper.rect(355, 360, 20, 60, 10);
paper.text(365, 390, "0\nM\nU\nX\n1");
var mux1_to_write_reg = paper.path("M375 390L400 390")



/********************** register file ***********************/
var registers = paper.rect(400, 300, 120, 140);
paper.text(460, 425, "Register\nFile").attr({"font-size":"12px", "font-weight":"bold"})
var read_register1 = paper.text(405, 315, "Read\nregister 1").attr("text-anchor","start");
var read_register2 = paper.text(405, 345, "Read\nregister 2").attr("text-anchor","start");
var write_register = paper.text(405, 385, "Write\nregister").attr("text-anchor","start");
var write_data = paper.text(405, 420, "Write\ndata").attr("text-anchor","start");
var read_data1 = paper.text(512, 330, "Read\ndata 1").attr("text-anchor","end");
var read_data2 = paper.text(512, 380, "Read\ndata 2").attr("text-anchor","end");

var reg_read_data1_to_alu = paper.path("M520 330L600 330").attr("stroke-dasharray", "-");
var reg_read_data2_to_mux2 = paper.path("M520 380L550 380").attr("stroke-dasharray", "-");
var reg_read_data2_to_data_mem_write_data = paper.path("M530 380L530 440L700 440").attr("stroke-dasharray", "-");


/******************** mux2 *************************/
var mux2 = paper.rect(550, 365, 20, 60, 10);
paper.text(560, 395, "0\nM\nU\nX\n1");
var mux2_to_alu = paper.path("M570 392L600 392");

/******************** control unit *******************/
var control_unit = paper.ellipse(400, 220, 30, 70, 5).attr("stroke", "#E69DF2");
paper.text(400, 220, "Control\nUnit").attr({"font-size":"12px", "font-weight":"bold","fill":"#E69DF2"});


var RegDst = paper.path("M376 180L100 180L100 450L365 450L365 420").attr({"stroke":"#E69DF2"});
var tRegDst = paper.text(355, 170, "RegDst").attr({"fill":"#E69DF2"});
var RegWrite = paper.path("M416 280L460 280L460 300").attr({"stroke":"#E69DF2"});
var tRegWrite = paper.text(460, 270, "RegWrite").attr({"fill":"#E69DF2"});
var ALUSrc = paper.path("M424 260L560 260L560 365").attr({"stroke":"#E69DF2"});
var tALUSrc = paper.text(460, 250, "ALUSrc").attr({"fill":"#E69DF2"});
var MemWrite = paper.path("M428 240L735 240L735 320").attr({"stroke":"#E69DF2"});
var tMemWrite = paper.text(460, 230, "MemWrite").attr({"fill":"#E69DF2"});
var ALUOp = paper.path("M430 220L585 220L585 500").attr({"stroke":"#E69DF2"});
var tALUOp = paper.text(460, 210, "ALUOp").attr({"fill":"#E69DF2"});
var MemtoReg = paper.path("M428 200L810 200L810 330").attr({"stroke":"#E69DF2"});
var tMemtoReg = paper.text(460, 190, "MemtoReg").attr({"fill":"#E69DF2"});
var MemRead = paper.path("M425 180L850 180L850 500L735 500L735 460").attr({"stroke":"#E69DF2"});
var tMemRead = paper.text(460, 170, "MemRead").attr({"fill":"#E69DF2"});
var Branch = paper.path("M415 160L670 160L670 120L700 120").attr({"stroke":"#E69DF2"});
var tBranch = paper.text(460, 150, "Branch").attr({"fill":"#E69DF2"});


/*********************** or  ******************************/

var or = paper.path("M700 110L700 150S760 130 700 110").attr({"stroke":"#E69DF2"});
var or_to_mux4 = paper.path("M726 130L750 130L750 110").attr({"stroke":"#E69DF2"});


/*********************** ALU2  ******************************/
var alu2 = paper.path("M580 60L650 75L650 125L580 140L580 105L590 100L580 95L580 60");
paper.text(605, 100, "ALU").attr({"font-size":"12px", "font-weight":"bold"});
var alu2_result = paper.text(645, 100, "ALU\nresult").attr("text-anchor","end");
var alu2_result_to_mux4 = paper.path("M650 100L 740 100");

/*********************** mux4  ******************************/;

var mux4 = paper.rect(740, 50, 20, 60, 10);
paper.text(750, 80, "0\nM\nU\nX\n1");
var mux4_to_pc = paper.path("M760 80L770 80L770 20L130 20L130 310L150 310");


/*********************** add ******************************/
var add = paper.path("M200 40L235 55L235 85L200 100L200 75L210 70L200 65L200 40");
paper.text(230, 70, "Add").attr("text-anchor","end");
paper.text(195, 55, '4').attr("text-anchor","end");
var add_to_alu2 = paper.path("M235 70L580 70");
var add_to_mux4 = paper.path("M235 70L500 70L500 50L700 50L740 60");
paper.text(700, 60, 'pc+4');


/********************** Data Memory *********************/
var data_memory = paper.rect(700, 320, 70, 140);
paper.text(735, 300, "Data\nMemory").attr({"font-size":"12px", "font-weight":"bold"});
var data_memory_addr = paper.text(705, 375, "address").attr("text-anchor","start");
var data_memory_write_data = paper.text(705, 440, "Write\ndata").attr("text-anchor","start");
var data_memory_read_data = paper.text(765, 340, "Read\ndata").attr("text-anchor","end");
var mem_read_data_to_mux3 = paper.path("M770 340L800 340");


/********************** mux3 *******************/
var mux3 = paper.rect(800, 330, 20, 60, 10);
paper.text(810, 360, "1\nM\nU\nX\n0");
var mux3_to_reg_write_data = paper.path("M820 360L 830 360L830 630L385 630L385 420L400 420");

/********************** ALU ******************/
var alu = paper.path("M600 310L670 335L670 385L600 410L600 365L610 360L600 355L600 310");
paper.text(625, 360, "ALU").attr({"font-size":"12px", "font-weight":"bold"});
var alu_result = paper.text(665, 375, "ALU\nresult").attr("text-anchor","end");
var alu_zero_to_or = paper.path('M670 345L685 345L685 140L700 140').attr({"stroke":"#E69DF2"});
var alu_result_to_addr = paper.path("M670 375L700 375");
var alu_result_to_mux3 = paper.path("M670 375L685 375L685 470L785 470L785 377L800 377");


/**************** sign extend **************/
var sign_extend = paper.ellipse(460, 530, 30, 50);
paper.text(460, 530, "Sign\nextend").attr({"font-size":"12px", "font-weight":"bold"});

var sign_extend_to_mux2 = paper.path("M490 530L540 530L540 412L550 412");
var sign_extend_to_alu2 = paper.path("M490 530L540 530L540 125L580 125");
paper.text(560, 140, "Shift\nleft 2");



/********************** ALU control **********************/

var alu_control = paper.ellipse(585, 550, 30, 50).attr({"stroke":"#E69DF2"});
paper.text(585, 550, "ALU\ncontrol").attr({"font-size":"12px", "font-weight":"bold", "fill":"#E69DF2"});
var control_alu =  paper.path("M615 550L635 550L635 398").attr({"stroke":"#E69DF2"});


/* finish painting, start to process */

var all_signals = paper.set();
all_signals.push(pc_to_read_addr);
all_signals.push(pc_to_add);


all_signals.push(read_address);
all_signals.push(op_to_control);
all_signals.push(op);
all_signals.push(rs);
all_signals.push(rs_to_read_reg1);
all_signals.push(rt_to_read_reg2);
all_signals.push(rt);
all_signals.push(imm_to_sign_extent);
all_signals.push(rt_to_mux1);
all_signals.push(rd_to_mux1);
all_signals.push(rd);
all_signals.push(funct_to_alu_control);


all_signals.push(mux1_to_write_reg);

all_signals.push(read_register1);
all_signals.push(read_register2);
all_signals.push(write_register);
all_signals.push(write_data);
all_signals.push(read_data1)
all_signals.push(read_data2);;
all_signals.push(reg_read_data1_to_alu);
all_signals.push(reg_read_data2_to_mux2);
all_signals.push(reg_read_data2_to_data_mem_write_data);


all_signals.push(mux2_to_alu);


all_signals.push(RegDst);
all_signals.push(RegWrite);
all_signals.push(ALUSrc);
all_signals.push(MemWrite);
all_signals.push(ALUOp);
all_signals.push(MemtoReg);
all_signals.push(MemRead);
all_signals.push(Branch);

all_signals.push(tRegDst);
all_signals.push(tRegWrite);
all_signals.push(tALUSrc);
all_signals.push(tMemWrite);
all_signals.push(tALUOp);
all_signals.push(tMemtoReg);
all_signals.push(tMemRead);
all_signals.push(tBranch);


all_signals.push(or_to_mux4);


all_signals.push(alu2_result_to_mux4);
all_signals.push(alu2_result);


all_signals.push(mux4_to_pc);


all_signals.push(add_to_alu2);
all_signals.push(add_to_mux4);


all_signals.push(data_memory_addr);
all_signals.push(data_memory_write_data);
all_signals.push(data_memory_read_data);
all_signals.push(mem_read_data_to_mux3);



all_signals.push(mux3_to_reg_write_data);

all_signals.push(alu_result);
all_signals.push(alu_zero_to_or);
all_signals.push(alu_result_to_addr);
all_signals.push(alu_result_to_mux3);


all_signals.push(sign_extend_to_mux2);
all_signals.push(sign_extend_to_alu2);


all_signals.push(control_alu);


/*********************** reset at the first time *********************/
reset();


/********************* toggle function ********************/

var rtype = paper.set()
rtype.push(RegDst);
rtype.push(tRegDst);
rtype.push(RegWrite);
rtype.push(tRegWrite);
rtype.push(ALUOp);
rtype.push(tALUOp);
rtype.push(rd_to_mux1);
rtype.push(rd);
rtype.push(rt_to_read_reg2);
rtype.push(rs_to_read_reg1);
rtype.push(mux1_to_write_reg);
rtype.push(write_register);
rtype.push(read_register1);
rtype.push(read_register2);
rtype.push(read_data1);
rtype.push(read_data2);
rtype.push(reg_read_data1_to_alu);
rtype.push(reg_read_data2_to_mux2);
rtype.push(mux2_to_alu);
rtype.push(control_alu);
rtype.push(alu_result);
rtype.push(alu_result_to_mux3);
rtype.push(mux3_to_reg_write_data);
rtype.push(pc_to_add);
rtype.push(add_to_mux4);
rtype.push(mux4_to_pc);


function runadd() {
    rtype.forEach(function (e) {
    e.attr({"stroke-opacity":1, "fill-opacity": 1})
    })
}

function reset() {
    all_signals.forEach(function (e) {
    e.attr({"stroke-opacity":0.1, "fill-opacity": 0.1})
})
}