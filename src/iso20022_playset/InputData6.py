import base_types
import InformationQualify1Code
import SaleCapabilities2Code
import InputCommand1Code
import ActionMessage11
import TrueFalseIndicator
import Number

class InputData6(base_types._BaseFieldType):

	__slots__ = ["_ImdtRspnFlg", "_WaitUsrVldtnFlg", "_BeepKeyFlg", "_DsblVldFlg", "_DsblCrrctFlg", "_DvcTp", "_DsblCclFlg", "_InfQlfr", "_NtfyCardInptFlg", "_MaxInptTm", "_MenuBckFlg", "_InptTxt", "_InptCmd", "_GblCrrctnFlg"]
	@property
	def ImdtRspnFlg(self):
		return self._ImdtRspnFlg

	@ImdtRspnFlg.setter
	def ImdtRspnFlg(self, value):
		self._ImdtRspnFlg = value if type(value) != auto else self.make_default("ImdtRspnFlg")

	@ImdtRspnFlg.deleter
	def ImdtRspnFlg(self):
		del self._ImdtRspnFlg
		self._ImdtRspnFlg = None

	@property
	def WaitUsrVldtnFlg(self):
		return self._WaitUsrVldtnFlg

	@WaitUsrVldtnFlg.setter
	def WaitUsrVldtnFlg(self, value):
		self._WaitUsrVldtnFlg = value if type(value) != auto else self.make_default("WaitUsrVldtnFlg")

	@WaitUsrVldtnFlg.deleter
	def WaitUsrVldtnFlg(self):
		del self._WaitUsrVldtnFlg
		self._WaitUsrVldtnFlg = None

	@property
	def BeepKeyFlg(self):
		return self._BeepKeyFlg

	@BeepKeyFlg.setter
	def BeepKeyFlg(self, value):
		self._BeepKeyFlg = value if type(value) != auto else self.make_default("BeepKeyFlg")

	@BeepKeyFlg.deleter
	def BeepKeyFlg(self):
		del self._BeepKeyFlg
		self._BeepKeyFlg = None

	@property
	def DsblVldFlg(self):
		return self._DsblVldFlg

	@DsblVldFlg.setter
	def DsblVldFlg(self, value):
		self._DsblVldFlg = value if type(value) != auto else self.make_default("DsblVldFlg")

	@DsblVldFlg.deleter
	def DsblVldFlg(self):
		del self._DsblVldFlg
		self._DsblVldFlg = None

	@property
	def DsblCrrctFlg(self):
		return self._DsblCrrctFlg

	@DsblCrrctFlg.setter
	def DsblCrrctFlg(self, value):
		self._DsblCrrctFlg = value if type(value) != auto else self.make_default("DsblCrrctFlg")

	@DsblCrrctFlg.deleter
	def DsblCrrctFlg(self):
		del self._DsblCrrctFlg
		self._DsblCrrctFlg = None

	@property
	def DvcTp(self):
		return self._DvcTp

	@DvcTp.setter
	def DvcTp(self, value):
		self._DvcTp = value if type(value) != auto else self.make_default("DvcTp")

	@DvcTp.deleter
	def DvcTp(self):
		del self._DvcTp
		self._DvcTp = None

	@property
	def DsblCclFlg(self):
		return self._DsblCclFlg

	@DsblCclFlg.setter
	def DsblCclFlg(self, value):
		self._DsblCclFlg = value if type(value) != auto else self.make_default("DsblCclFlg")

	@DsblCclFlg.deleter
	def DsblCclFlg(self):
		del self._DsblCclFlg
		self._DsblCclFlg = None

	@property
	def InfQlfr(self):
		return self._InfQlfr

	@InfQlfr.setter
	def InfQlfr(self, value):
		self._InfQlfr = value if type(value) != auto else self.make_default("InfQlfr")

	@InfQlfr.deleter
	def InfQlfr(self):
		del self._InfQlfr
		self._InfQlfr = None

	@property
	def NtfyCardInptFlg(self):
		return self._NtfyCardInptFlg

	@NtfyCardInptFlg.setter
	def NtfyCardInptFlg(self, value):
		self._NtfyCardInptFlg = value if type(value) != auto else self.make_default("NtfyCardInptFlg")

	@NtfyCardInptFlg.deleter
	def NtfyCardInptFlg(self):
		del self._NtfyCardInptFlg
		self._NtfyCardInptFlg = None

	@property
	def MaxInptTm(self):
		return self._MaxInptTm

	@MaxInptTm.setter
	def MaxInptTm(self, value):
		self._MaxInptTm = value if type(value) != auto else self.make_default("MaxInptTm")

	@MaxInptTm.deleter
	def MaxInptTm(self):
		del self._MaxInptTm
		self._MaxInptTm = None

	@property
	def MenuBckFlg(self):
		return self._MenuBckFlg

	@MenuBckFlg.setter
	def MenuBckFlg(self, value):
		self._MenuBckFlg = value if type(value) != auto else self.make_default("MenuBckFlg")

	@MenuBckFlg.deleter
	def MenuBckFlg(self):
		del self._MenuBckFlg
		self._MenuBckFlg = None

	@property
	def InptTxt(self):
		return self._InptTxt

	@InptTxt.setter
	def InptTxt(self, value):
		self._InptTxt = value if type(value) != auto else self.make_default("InptTxt")

	@InptTxt.deleter
	def InptTxt(self):
		del self._InptTxt
		self._InptTxt = None

	@property
	def InptCmd(self):
		return self._InptCmd

	@InptCmd.setter
	def InptCmd(self, value):
		self._InptCmd = value if type(value) != auto else self.make_default("InptCmd")

	@InptCmd.deleter
	def InptCmd(self):
		del self._InptCmd
		self._InptCmd = None

	@property
	def GblCrrctnFlg(self):
		return self._GblCrrctnFlg

	@GblCrrctnFlg.setter
	def GblCrrctnFlg(self, value):
		self._GblCrrctnFlg = value if type(value) != auto else self.make_default("GblCrrctnFlg")

	@GblCrrctnFlg.deleter
	def GblCrrctnFlg(self):
		del self._GblCrrctnFlg
		self._GblCrrctnFlg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ImdtRspnFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WaitUsrVldtnFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BeepKeyFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DsblVldFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DsblCrrctFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DvcTp', type=SaleCapabilities2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DsblCclFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfQlfr', type=InformationQualify1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfyCardInptFlg', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxInptTm', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MenuBckFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InptTxt', type=ActionMessage11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InptCmd', type=InputCommand1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GblCrrctnFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))

