

var paper = Raphael(document.getElementById("circuit"), 960, 650);

/********************************* PC *******************************/
var pc =paper.rect(150, 285, 20, 50);
paper.text(150+10, 285+25, "pc").attr({"font-size":"12px", "font-weight":"bold"});
var pc_to_read_addr = paper.path("M170, 310L198 310").attr("arrow-end", "block-wide-long");
var pc_to_add = paper.path("M170 310L185 310L185 85L198 85").attr("arrow-end", "block-wide-long");


/********************* Instruction Memory *********************/

var inst_memory = paper.rect(200, 300, 70, 100);
paper.text(235, 350, "Instruction\nMemory").attr({"font-size":"12px", "font-weight":"bold"});

var read_address = paper.text(205, 312, "Read\naddress").attr("text-anchor","start");
var op_to_control = paper.path("M280 350L280 200L370 200").attr("arrow-end", "block-wide-long");
var op = paper.text(285, 192, "Instruction[31:26]").attr("text-anchor","start");
var rs_to_read_reg1 = paper.path("M270 350L280 350L280 320L398 320").attr("arrow-end", "block-wide-long");
var rs = paper.text(285, 312, "Instruction[25:21]").attr("text-anchor","start");
var rt_to_read_reg2 = paper.path("M280 350L398 350").attr("arrow-end", "block-wide-long");
var rt = paper.text(285, 342, "Instruction[20:16]").attr("text-anchor","start");
var rt_to_mux1 = paper.path("M270 350L325 350L325 372L353 372").attr("arrow-end", "block-wide-long");
var imm_to_sign_extent = paper.path("M270 350L280 350L280 530L428 530").attr("stroke-dasharray", "-").attr("arrow-end", "block-wide-long");
var imm = paper.text(285, 540, "Instruction[15:0]").attr("text-anchor","start");
var rd_to_mux1 = paper.path("M270 350L280 350L280 407L353 407").attr("arrow-end", "block-wide-long");
var rd = paper.text(285, 430, "Instruction[15:11]").attr("text-anchor","start");
var funct_to_alu_control = paper.path("M270 350L280 350L280 530L400 530L400 550L553 550").attr("stroke-dasharray", "-").attr("arrow-end", "block-wide-long");
var funct = paper.text(520, 560, "Instruction[5:0]");
var address_to_mux5 = paper.path("M270 350L280 350L280 55L272 55").attr("arrow-end", "block-wide-long");
var address = paper.text(285, 120, "Instruction[25:0]").attr("text-anchor","start");
paper.text(285, 100, "<< 2").attr("text-anchor","start");

/************************  mux1 ***************************/
var mux1 =paper.rect(355, 360, 20, 60, 10);
paper.text(365, 390, "0\nM\nU\nX\n1");
var mux1_to_write_reg = paper.path("M375 390L398 390").attr("arrow-end", "block-wide-long");



/********************** register file ***********************/
var registers = paper.rect(400, 300, 120, 140);
paper.text(460, 425, "Register\nFile").attr({"font-size":"12px", "font-weight":"bold"})
var read_register1 = paper.text(405, 315, "Read\nregister 1").attr("text-anchor","start");
var read_register2 = paper.text(405, 345, "Read\nregister 2").attr("text-anchor","start");
var write_register = paper.text(405, 385, "Write\nregister").attr("text-anchor","start");
var write_data = paper.text(405, 420, "Write\ndata").attr("text-anchor","start");
var read_data1 = paper.text(512, 330, "Read\ndata 1").attr("text-anchor","end");
var read_data2 = paper.text(512, 380, "Read\ndata 2").attr("text-anchor","end");

var reg_read_data1_to_alu = paper.path("M520 330L598 330").attr("stroke-dasharray", "-").attr("arrow-end", "block-wide-long");
var reg_read_data2_to_mux2 = paper.path("M520 380L548 380").attr("stroke-dasharray", "-").attr("arrow-end", "block-wide-long");
var reg_read_data2_to_data_mem_write_data = paper.path("M520 380L530 380L530 440L698 440").attr("stroke-dasharray", "-").attr("arrow-end", "block-wide-long");


/******************** mux2 *************************/
var mux2 = paper.rect(550, 365, 20, 60, 10);
paper.text(560, 395, "0\nM\nU\nX\n1");
var mux2_to_alu = paper.path("M570 392L598 392").attr("arrow-end", "block-wide-long");

/******************** control unit *******************/
var control_unit = paper.ellipse(400, 220, 30, 70, 5).attr("stroke", "#E69DF2");
paper.text(400, 220, "Control\nUnit").attr({"font-size":"12px", "font-weight":"bold","fill":"#E69DF2"});


var RegDst = paper.path("M376 180L100 180L100 450L365 450L365 420").attr({"stroke":"#E69DF2"});
var tRegDst = paper.text(355, 170, "RegDst").attr({"fill":"#E69DF2"});
var Jump = paper.path("M384 160L260 160L260 62").attr({"stroke":"#1BDDE0"});
var tJump = paper.text(355, 150, "Jump").attr({"fill":"#1BDDE0"});
var RegWrite = paper.path("M416 280L460 280L460 300").attr({"stroke":"#8B52FF"});
var tRegWrite = paper.text(460, 270, "RegWrite").attr({"fill":"#8B52FF"});
var ALUSrc = paper.path("M424 260L560 260L560 365").attr({"stroke":"#1B44CC"});
var tALUSrc = paper.text(460, 250, "ALUSrc").attr({"fill":"#1B44CC"});
var MemWrite = paper.path("M428 240L735 240L735 320").attr({"stroke":"#E69DF2"});
var tMemWrite = paper.text(460, 230, "MemWrite").attr({"fill":"#E69DF2"});
var ALUOp = paper.path("M430 220L585 220L585 500").attr({"stroke":"#47CC1B"});
var tALUOp = paper.text(460, 210, "ALUOp").attr({"fill":"#47CC1B"});
var MemtoReg = paper.path("M428 200L810 200L810 330").attr({"stroke":"#F2D322"});
var tMemtoReg = paper.text(460, 190, "MemtoReg").attr({"fill":"#F2D322"});
var MemRead = paper.path("M425 180L850 180L850 500L735 500L735 460").attr({"stroke":"#FFA852"});
var tMemRead = paper.text(460, 170, "MemRead").attr({"fill":"#FFA852"});
var Branch = paper.path("M415 160L670 160L670 120L700 120").attr({"stroke":"#CC1B2F"});
var tBranch = paper.text(460, 150, "Branch").attr({"fill":"#CC1B2F"});




/*********************** or  ******************************/

var or = paper.path("M700 110L700 150S760 130 700 110").attr({"stroke":"#E69DF2"});
var or_to_mux4 = paper.path("M726 130L750 130L750 110").attr({"stroke":"#E69DF2"});
var or_mark = paper.text(740, 130, "?");

/*********************** ALU2  ******************************/
var alu2 = paper.path("M580 60L650 75L650 125L580 140L580 105L590 100L580 95L580 60");
paper.text(605, 100, "ALU").attr({"font-size":"12px", "font-weight":"bold"});
var alu2_result = paper.text(645, 100, "ALU\nresult").attr("text-anchor","end");
var alu2_result_value = paper.text(660, 90, "imm << 2 + pc").attr("text-anchor","start"); 
var alu2_result_to_mux4 = paper.path("M650 100L 738 100").attr("arrow-end", "block-wide-long");

/*********************** mux4  ******************************/;

var mux4 = paper.rect(740, 50, 20, 60, 10);
paper.text(750, 80, "0\nM\nU\nX\n1");
var mux4_to_mux5 = paper.path("M760 80L770 80L770 15L272 15").attr("arrow-end", "block-wide-long");


/*********************** add ******************************/
var add = paper.path("M200 40L235 55L235 85L200 100L200 75L210 70L200 65L200 40");
paper.text(230, 70, "Add").attr("text-anchor","end");
paper.text(195, 55, '4').attr("text-anchor","end");
var add_to_alu2 = paper.path("M235 70L578 70").attr("arrow-end", "block-wide-long");
var add_to_mux4 = paper.path("M235 70L500 70L500 50L700 50L738 60").attr("arrow-end", "block-wide-long");
paper.text(700, 60, 'pc+4');
var add_bus = paper.path("M235 70L280 70").attr("arrow-end", "block-wide-long");
var add_target = paper.text(255, 90, "pc+4\n[31:28]");

/********************** Data Memory *********************/
var data_memory = paper.rect(700, 320, 70, 140);
paper.text(735, 300, "Data\nMemory").attr({"font-size":"12px", "font-weight":"bold"});
var data_memory_addr = paper.text(705, 375, "address").attr("text-anchor","start");
var data_memory_write_data = paper.text(705, 440, "Write\ndata").attr("text-anchor","start");
var data_memory_read_data = paper.text(765, 340, "Read\ndata").attr("text-anchor","end");
var mem_read_data_to_mux3 = paper.path("M770 340L798 340").attr("arrow-end", "block-wide-long");


/********************** mux3 *******************/
var mux3 = paper.rect(800, 330, 20, 60, 10);
paper.text(810, 360, "1\nM\nU\nX\n0");
var mux3_to_reg_write_data = paper.path("M820 360L 830 360L830 630L385 630L385 420L398 420").attr("arrow-end", "block-wide-long");

/********************** ALU ******************/
var alu = paper.path("M600 310L670 335L670 385L600 410L600 365L610 360L600 355L600 310");
paper.text(625, 360, "ALU").attr({"font-size":"12px", "font-weight":"bold"});
var alu_result = paper.text(665, 375, "ALU\nresult").attr("text-anchor","end");
var alu_zero = paper.text(665, 345, "Zero").attr("text-anchor","end");
var alu_zero_to_or = paper.path('M670 345L685 345L685 140L700 140').attr({"stroke":"#E69DF2"});
var alu_result_to_addr = paper.path("M670 375L698 375").attr("arrow-end", "block-wide-long");
var alu_result_to_mux3 = paper.path("M670 375L685 375L685 470L785 470L785 377L798 377").attr("arrow-end", "block-wide-long");


/**************** sign extend **************/
var sign_extend = paper.ellipse(460, 530, 30, 50);
paper.text(460, 530, "Sign\nextend").attr({"font-size":"12px", "font-weight":"bold"});
paper.text(420, 520, "16");
paper.text(500, 520, "32");
var sign_extend_to_mux2 = paper.path("M490 530L540 530L540 412L548 412").attr("arrow-end", "block-wide-long");
var sign_extend_to_alu2 = paper.path("M490 530L540 530L540 125L578 125").attr("arrow-end", "block-wide-long");
paper.text(560, 140, "<< 2");



/********************** ALU control **********************/

var alu_control = paper.ellipse(585, 550, 30, 50).attr({"stroke":"#E69DF2"});
paper.text(585, 550, "ALU\ncontrol").attr({"font-size":"12px", "font-weight":"bold", "fill":"#E69DF2"});
var control_alu =  paper.path("M615 550L635 550L635 398").attr({"stroke":"#E69DF2"});


/******************************** mux5 ********************************/
var mux5 = paper.rect(250, 3, 20, 60, 10);
paper.text(260, 33, "0\nM\nU\nX\n1");
var mux5_to_pc = paper.path("M250 30L130 30L130 310L148 310").attr("arrow-end", "block-wide-long");
/******************** finish painting, start to process ****************/

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
all_signals.push(imm);
all_signals.push(imm_to_sign_extent);
all_signals.push(rt_to_mux1);
all_signals.push(rd_to_mux1);
all_signals.push(rd);
all_signals.push(funct_to_alu_control);
all_signals.push(funct);
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
all_signals.push(or_mark);
all_signals.push(alu2_result_to_mux4);
all_signals.push(alu2_result);
all_signals.push(alu2_result_value);
all_signals.push(add_to_alu2);
all_signals.push(add_to_mux4);
all_signals.push(data_memory_addr);
all_signals.push(data_memory_write_data);
all_signals.push(data_memory_read_data);
all_signals.push(mem_read_data_to_mux3);
all_signals.push(mux3_to_reg_write_data);
all_signals.push(alu_result);
all_signals.push(alu_zero);
all_signals.push(alu_zero_to_or);
all_signals.push(alu_result_to_addr);
all_signals.push(alu_result_to_mux3);
all_signals.push(sign_extend_to_mux2);
all_signals.push(sign_extend_to_alu2);
all_signals.push(control_alu);
all_signals.push(mux5_to_pc);
all_signals.push(address_to_mux5);
all_signals.push(Jump);
all_signals.push(tJump);
all_signals.push(mux4_to_mux5);
all_signals.push(address);
all_signals.push(add_bus);
all_signals.push(add_target);

/*********************** reset at the first time *********************/
reset();


/**************************** toggle function ***********************/

function reset() {
    all_signals.forEach(function (e) {
        e.attr({"stroke-opacity":0.3,  "opacity": 0.2});
    })
}


function runRtype() {
    enableFixed();
    enableRegDst();
    disableALUSrc();
    disableMemtoReg();
    enableRegWrite();
    disableMemRead();
    disableMemWrite();
    disableBranch();
    enableALUOp();
}


function runAddi() {
    enableFixed();
    enableRegWrite();
    disableRegDst();
    enableALUSrc();
    disableBranch();
    disableMemWrite();
    disableMemRead();
    disableMemtoReg();
    enableALUOp();
    
}

function runLw() {
    enableFixed();
    disableRegDst();
    enableALUSrc();
    enableMemtoReg();
    enableRegWrite();
    enableMemRead();
    disableMemWrite();
    enableALUOp();
    disableBranch();
}

function runSw() {
    enableFixed();
    //disableRegDst();
    enableALUSrc();
    //enableMemtoReg();
    disableRegWrite();
    disableMemRead();
    enableMemWrite();
    enableALUOp();
    disableBranch();
}

function runBeq() {
    enableFixed();
    //disableRegDst();
    disableALUSrc();
    //enableMemtoReg();
    disableRegWrite();
    disableMemRead();
    disableMemWrite();
    enableALUOp();
    enableBranch();
}

function runJ() {
    enableFixed();
    enableJump();
    disableRegWrite();
    disableMemWrite();
}

/************************ enable signals ************************/
function enableFixed() {
    var fixed = paper.set();
    fixed.push(read_address);
    fixed.push(pc_to_read_addr);
    fixed.push(op_to_control);
    fixed.push(op);
    fixed.push(rs);
    fixed.push(rs_to_read_reg1);
    fixed.push(rt);
    fixed.push(rt_to_read_reg2);
    fixed.push(read_register1);
    fixed.push(read_register2);
    fixed.push(read_data1);
    fixed.push(reg_read_data1_to_alu);
    fixed.forEach(function (e) {
        e.attr({"stroke-opacity":1, "opacity": 1})
    })
}


function enableRegWrite() {
    var rw = paper.set();
    rw.push(RegWrite);
    rw.push(tRegWrite);
    rw.push(write_data);
    rw.push(mux3_to_reg_write_data);
    rw.forEach(function (e) {
        e.attr({"stroke-opacity":1, "opacity": 1})
    })
}

function disableRegWrite() {}

function enableRegDst() {
    var rs = paper.set();
    rs.push(RegDst);
    rs.push(tRegDst);
    rs.push(mux1_to_write_reg);
    rs.push(rd_to_mux1);
    rs.push(rd);
    rs.push(write_register);
    rs.forEach(function (e) {
        e.attr({"stroke-opacity":1, "opacity": 1})
    })
}

function disableRegDst() {
    var rs = paper.set();
    rs.push(mux1_to_write_reg);
    rs.push(rt_to_mux1);
    rs.push(rt);
    rs.push(write_register);
    rs.forEach(function (e) {
        e.attr({"stroke-opacity":1, "opacity": 1})
    })
}

function enableALUSrc() {
    var as = paper.set();
    as.push(ALUSrc);
    as.push(tALUSrc);
    as.push(mux2_to_alu);
    as.push(sign_extend_to_mux2);
    as.push(imm_to_sign_extent);
    as.push(imm);  
    as.forEach(function (e) {
        e.attr({"stroke-opacity":1, "opacity": 1})
    })
}

function disableALUSrc() {
    var as = paper.set();
    as.push(reg_read_data2_to_mux2);
    as.push(read_data2);
    as.push(mux2_to_alu);
    as.forEach(function (e) {
        e.attr({"stroke-opacity":1, "opacity": 1})
    })
}

function enableALUOp() {
    var ao = paper.set();
    ao.push(ALUOp);
    ao.push(tALUOp);
    ao.push(control_alu);
    ao.forEach(function (e) {
        e.attr({"stroke-opacity":1, "opacity": 1})
    })

}

function disableALUOp() {}


function enableMemtoReg() {
    var mr = paper.set();
    mr.push(MemtoReg);
    mr.push(tMemtoReg);
    mr.push(mem_read_data_to_mux3);
    mr.forEach(function (e) {
        e.attr({"stroke-opacity":1, "opacity": 1})
    })

}

function disableMemtoReg() {
    var mr = paper.set();
    mr.push(alu_result);
    mr.push(alu_result_to_mux3);

    mr.forEach(function (e) {
        e.attr({"stroke-opacity":1, "opacity": 1})
    })
}

function enableMemRead() {
    var mr = paper.set();
    mr.push(MemRead);
    mr.push(tMemRead);
    mr.push(alu_result_to_addr);
    mr.push(alu_result);
    mr.push(data_memory_addr);
    mr.push(data_memory_read_data);
    mr.forEach(function (e) {
        e.attr({"stroke-opacity":1, "opacity": 1})
    })
}

function disableMemRead() {
}

function enableMemWrite() {
    var mw = paper.set();
    mw.push(MemWrite);
    mw.push(tMemWrite);
    mw.push(data_memory_write_data);
    mw.push(data_memory_addr);
    mw.push(read_data2);
    mw.push(reg_read_data2_to_data_mem_write_data);
    mw.push(alu_result_to_addr);
    mw.push(alu_result);
    mw.forEach(function (e) {
        e.attr({"stroke-opacity":1, "opacity": 1})
    })
}

function disableMemWrite() {}

function enableBranch() {
    var br = paper.set();
    br.push(Branch);
    br.push(tBranch);
    br.push(or_to_mux4);
    br.push(mux4_to_mux5);
    br.push(mux5_to_pc);
    br.push(alu2_result_to_mux4);
    br.push(alu2_result);
    br.push(sign_extend_to_alu2);
    br.push(imm_to_sign_extent);
    br.push(imm);
    br.push(pc_to_add);
    br.push(add_to_alu2);
    br.push(alu_zero_to_or);
    br.push(add_to_mux4);
    br.push(or_mark);
    br.push(alu2_result_value); 
    br.push(alu_zero); 
    br.forEach(function (e) {
        e.attr({"stroke-opacity":1, "opacity": 1})
    })
}

function disableBranch() {
    var br = paper.set();
    br.push(pc_to_add);
    br.push(add_to_mux4);
    br.push(mux4_to_mux5);
    br.push(mux5_to_pc);
    br.push(funct);
    br.push(funct_to_alu_control);
    br.forEach(function (e) {
        e.attr({"stroke-opacity":1, "opacity": 1})
    })
}


function enableJump() {
    var jp = paper.set();
    jp.push(Jump);
    jp.push(tJump);
    jp.push(address_to_mux5);
    jp.push(mux5_to_pc);
    jp.push(address);
    jp.push(add_bus);
    jp.push(add_target);
    jp.forEach(function (e) {
        e.attr({"stroke-opacity":1, "opacity": 1})
    })
}

function disableJump() {
}