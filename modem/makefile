PROJECT := AEON6737M_65_M0
PROJECT_MAKEFILE_CONFIG:=AEON6737M_65_M0\(LWG_DSDS_COTSX\).mak
INSTALL_BIN :=out/$(PROJECT)

# eval 拷贝modem编译文件
# Args:
#    $(1)  编辑文件目录
#    $(2)  源文件
#    $(3)  源文件后缀
#    $(4)  目标文件

define copy-built-modem-file
$(shell mkdir -p $(INSTALL_BIN))
$(eval f=$(shell find $(1) -type f -name $(2) -print))
$(eval new_file=$(patsubst %.$(3),%_1_lwg_n.$(3),$(notdir ${f}) ) )
$(if $(4),$(shell install -c $(f) $(INSTALL_BIN)/$(4)),$(shell install -c $(f) $(INSTALL_BIN)/$(new_file) ) )
@ if [ -n "$(4)" ]; then\
	echo "copy modem file $(f)=>$(INSTALL_BIN)/$(4)"; \
else  \
	echo "copy modem file $(f)=>$(INSTALL_BIN)/$(new_file)"; \
fi
endef

define copy-built-modem-file2
$(shell mkdir -p $(INSTALL_BIN))
$(eval f=$(shell find $(1) -type f -name $(2) -print ) )
$(eval new_file=$(addsuffix _1_lwg_n,$(notdir ${f}) ) )
$(shell install -c $(f) $(INSTALL_BIN)/$(new_file))
@echo "copy modem file: $(f)=>$(INSTALL_BIN)/$(new_file)"
endef

define copy-built-modem-file3
$(shell mkdir -p $(INSTALL_BIN))
$(eval f=$(shell find $(1) -type f -name $(2) -print))
$(shell find $(1) -type f -name $(2) -print | xargs -i install -c  {} $(INSTALL_BIN)/$(3) )
@echo "copy modem file: $(f)=>$(INSTALL_BIN)/$(3)"
endef

all:
	@echo "Build modem ..."
	./m $(PROJECT_MAKEFILE_CONFIG) new

clean:
	@echo "Clean modem ..."
	./m $(PROJECT_MAKEFILE_CONFIG) clean


install:
	$(call copy-built-modem-file, "./build", "catcher_filter.bin",bin)
	$(call copy-built-modem-file2, "./build", "BPMdMetaDatabase*")
	$(call copy-built-modem-file, "./build", "em_filter.bin",bin)
	$(call copy-built-modem-file, "./build", "mdm_layout_desc.dat",dat)
	$(call copy-built-modem-file, "./build/$(PROJECT)/LWG_DSDS_COTSX/bin", "*MDBIN_PCB01_*bin",bin,modem_1_lwg_n.img)
	$(call copy-built-modem-file2, "./build/$(PROJECT)/LWG_DSDS_COTSX/bin", "DbgInfo_LR*")
	$(call copy-built-modem-file, "./build/$(PROJECT)/LWG_DSDS_COTSX/bin", "*DSP*",bin,dsp_1_lwg_n.bin)
	$(call copy-built-modem-file3, "./build/$(PROJECT)/LWG_DSDS_COTSX/bin", "~$(PROJECT_MAKEFILE_CONFIG)",modem_1_ulwctg_n.mak)
