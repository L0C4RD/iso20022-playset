# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActionMessage12
from . import InformationQualify1Code
from . import InputCommand1Code
from . import Number
from . import SaleCapabilities2Code
from . import TrueFalseIndicator

class InputData7(base_types._BaseFieldType):

	__slots__ = ["_BeepKeyFlg", "_DsblCclFlg", "_DsblCrrctFlg", "_DsblVldFlg", "_DvcTp", "_GblCrrctnFlg", "_ImdtRspnFlg", "_InfQlfr", "_InptCmd", "_InptTxt", "_MaxInptTm", "_MenuBckFlg", "_NtfyCardInptFlg", "_WaitUsrVldtnFlg"]
	@property
	def BeepKeyFlg(self):
		return self._BeepKeyFlg

	@BeepKeyFlg.setter
	def BeepKeyFlg(self, value):
		self._BeepKeyFlg = value if value is not None else base_types.UninitialisedField(self, 'BeepKeyFlg', TrueFalseIndicator, False)

	@BeepKeyFlg.deleter
	def BeepKeyFlg(self):
		del self._BeepKeyFlg
		self._BeepKeyFlg = base_types.UninitialisedField(self, 'BeepKeyFlg', TrueFalseIndicator, False)

	@property
	def DsblCclFlg(self):
		return self._DsblCclFlg

	@DsblCclFlg.setter
	def DsblCclFlg(self, value):
		self._DsblCclFlg = value if value is not None else base_types.UninitialisedField(self, 'DsblCclFlg', TrueFalseIndicator, False)

	@DsblCclFlg.deleter
	def DsblCclFlg(self):
		del self._DsblCclFlg
		self._DsblCclFlg = base_types.UninitialisedField(self, 'DsblCclFlg', TrueFalseIndicator, False)

	@property
	def DsblCrrctFlg(self):
		return self._DsblCrrctFlg

	@DsblCrrctFlg.setter
	def DsblCrrctFlg(self, value):
		self._DsblCrrctFlg = value if value is not None else base_types.UninitialisedField(self, 'DsblCrrctFlg', TrueFalseIndicator, False)

	@DsblCrrctFlg.deleter
	def DsblCrrctFlg(self):
		del self._DsblCrrctFlg
		self._DsblCrrctFlg = base_types.UninitialisedField(self, 'DsblCrrctFlg', TrueFalseIndicator, False)

	@property
	def DsblVldFlg(self):
		return self._DsblVldFlg

	@DsblVldFlg.setter
	def DsblVldFlg(self, value):
		self._DsblVldFlg = value if value is not None else base_types.UninitialisedField(self, 'DsblVldFlg', TrueFalseIndicator, False)

	@DsblVldFlg.deleter
	def DsblVldFlg(self):
		del self._DsblVldFlg
		self._DsblVldFlg = base_types.UninitialisedField(self, 'DsblVldFlg', TrueFalseIndicator, False)

	@property
	def DvcTp(self):
		return self._DvcTp

	@DvcTp.setter
	def DvcTp(self, value):
		self._DvcTp = value if value is not None else base_types.UninitialisedField(self, 'DvcTp', SaleCapabilities2Code, False)

	@DvcTp.deleter
	def DvcTp(self):
		del self._DvcTp
		self._DvcTp = base_types.UninitialisedField(self, 'DvcTp', SaleCapabilities2Code, False)

	@property
	def GblCrrctnFlg(self):
		return self._GblCrrctnFlg

	@GblCrrctnFlg.setter
	def GblCrrctnFlg(self, value):
		self._GblCrrctnFlg = value if value is not None else base_types.UninitialisedField(self, 'GblCrrctnFlg', TrueFalseIndicator, False)

	@GblCrrctnFlg.deleter
	def GblCrrctnFlg(self):
		del self._GblCrrctnFlg
		self._GblCrrctnFlg = base_types.UninitialisedField(self, 'GblCrrctnFlg', TrueFalseIndicator, False)

	@property
	def ImdtRspnFlg(self):
		return self._ImdtRspnFlg

	@ImdtRspnFlg.setter
	def ImdtRspnFlg(self, value):
		self._ImdtRspnFlg = value if value is not None else base_types.UninitialisedField(self, 'ImdtRspnFlg', TrueFalseIndicator, False)

	@ImdtRspnFlg.deleter
	def ImdtRspnFlg(self):
		del self._ImdtRspnFlg
		self._ImdtRspnFlg = base_types.UninitialisedField(self, 'ImdtRspnFlg', TrueFalseIndicator, False)

	@property
	def InfQlfr(self):
		return self._InfQlfr

	@InfQlfr.setter
	def InfQlfr(self, value):
		self._InfQlfr = value if value is not None else base_types.UninitialisedField(self, 'InfQlfr', InformationQualify1Code, False)

	@InfQlfr.deleter
	def InfQlfr(self):
		del self._InfQlfr
		self._InfQlfr = base_types.UninitialisedField(self, 'InfQlfr', InformationQualify1Code, False)

	@property
	def InptCmd(self):
		return self._InptCmd

	@InptCmd.setter
	def InptCmd(self, value):
		self._InptCmd = value if value is not None else base_types.UninitialisedField(self, 'InptCmd', InputCommand1Code, False)

	@InptCmd.deleter
	def InptCmd(self):
		del self._InptCmd
		self._InptCmd = base_types.UninitialisedField(self, 'InptCmd', InputCommand1Code, False)

	@property
	def InptTxt(self):
		return self._InptTxt

	@InptTxt.setter
	def InptTxt(self, value):
		self._InptTxt = value if value is not None else base_types.UninitialisedField(self, 'InptTxt', ActionMessage12, False)

	@InptTxt.deleter
	def InptTxt(self):
		del self._InptTxt
		self._InptTxt = base_types.UninitialisedField(self, 'InptTxt', ActionMessage12, False)

	@property
	def MaxInptTm(self):
		return self._MaxInptTm

	@MaxInptTm.setter
	def MaxInptTm(self, value):
		self._MaxInptTm = value if value is not None else base_types.UninitialisedField(self, 'MaxInptTm', Number, False)

	@MaxInptTm.deleter
	def MaxInptTm(self):
		del self._MaxInptTm
		self._MaxInptTm = base_types.UninitialisedField(self, 'MaxInptTm', Number, False)

	@property
	def MenuBckFlg(self):
		return self._MenuBckFlg

	@MenuBckFlg.setter
	def MenuBckFlg(self, value):
		self._MenuBckFlg = value if value is not None else base_types.UninitialisedField(self, 'MenuBckFlg', TrueFalseIndicator, False)

	@MenuBckFlg.deleter
	def MenuBckFlg(self):
		del self._MenuBckFlg
		self._MenuBckFlg = base_types.UninitialisedField(self, 'MenuBckFlg', TrueFalseIndicator, False)

	@property
	def NtfyCardInptFlg(self):
		return self._NtfyCardInptFlg

	@NtfyCardInptFlg.setter
	def NtfyCardInptFlg(self, value):
		self._NtfyCardInptFlg = value if value is not None else base_types.UninitialisedField(self, 'NtfyCardInptFlg', TrueFalseIndicator, False)

	@NtfyCardInptFlg.deleter
	def NtfyCardInptFlg(self):
		del self._NtfyCardInptFlg
		self._NtfyCardInptFlg = base_types.UninitialisedField(self, 'NtfyCardInptFlg', TrueFalseIndicator, False)

	@property
	def WaitUsrVldtnFlg(self):
		return self._WaitUsrVldtnFlg

	@WaitUsrVldtnFlg.setter
	def WaitUsrVldtnFlg(self, value):
		self._WaitUsrVldtnFlg = value if value is not None else base_types.UninitialisedField(self, 'WaitUsrVldtnFlg', TrueFalseIndicator, False)

	@WaitUsrVldtnFlg.deleter
	def WaitUsrVldtnFlg(self):
		del self._WaitUsrVldtnFlg
		self._WaitUsrVldtnFlg = base_types.UninitialisedField(self, 'WaitUsrVldtnFlg', TrueFalseIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BeepKeyFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DsblCclFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DsblCrrctFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DsblVldFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DvcTp', type=SaleCapabilities2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GblCrrctnFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ImdtRspnFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfQlfr', type=InformationQualify1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InptCmd', type=InputCommand1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InptTxt', type=ActionMessage12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxInptTm', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MenuBckFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfyCardInptFlg', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WaitUsrVldtnFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))