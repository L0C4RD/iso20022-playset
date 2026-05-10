from . import base_types
from ._ConfirmationPartyDetails12 import ConfirmationPartyDetails12
from ._ConfirmationPartyDetails13 import ConfirmationPartyDetails13
from ._ConfirmationPartyDetails11 import ConfirmationPartyDetails11
from ._ConfirmationPartyDetails14 import ConfirmationPartyDetails14

class ConfirmationParties7(base_types._BaseFieldType):

	__slots__ = ["_Brrwr", "_Sellr", "_StepOutFirm", "_ClrFirm", "_CMUPty", "_AffrmgPty", "_CMUCtrPty", "_ExctgBrkr", "_Lndr", "_Buyr", "_TradBnfcryPty", "_StepInFirm", "_BrkrOfCdt", "_IntrdcgFirm"]
	@property
	def Brrwr(self):
		return self._Brrwr

	@Brrwr.setter
	def Brrwr(self, value):
		self._Brrwr = value if type(value) != base_types.auto else self.make_default("Brrwr")

	@Brrwr.deleter
	def Brrwr(self):
		del self._Brrwr
		self._Brrwr = None

	@property
	def Sellr(self):
		return self._Sellr

	@Sellr.setter
	def Sellr(self, value):
		self._Sellr = value if type(value) != base_types.auto else self.make_default("Sellr")

	@Sellr.deleter
	def Sellr(self):
		del self._Sellr
		self._Sellr = None

	@property
	def StepOutFirm(self):
		return self._StepOutFirm

	@StepOutFirm.setter
	def StepOutFirm(self, value):
		self._StepOutFirm = value if type(value) != base_types.auto else self.make_default("StepOutFirm")

	@StepOutFirm.deleter
	def StepOutFirm(self):
		del self._StepOutFirm
		self._StepOutFirm = None

	@property
	def ClrFirm(self):
		return self._ClrFirm

	@ClrFirm.setter
	def ClrFirm(self, value):
		self._ClrFirm = value if type(value) != base_types.auto else self.make_default("ClrFirm")

	@ClrFirm.deleter
	def ClrFirm(self):
		del self._ClrFirm
		self._ClrFirm = None

	@property
	def CMUPty(self):
		return self._CMUPty

	@CMUPty.setter
	def CMUPty(self, value):
		self._CMUPty = value if type(value) != base_types.auto else self.make_default("CMUPty")

	@CMUPty.deleter
	def CMUPty(self):
		del self._CMUPty
		self._CMUPty = None

	@property
	def AffrmgPty(self):
		return self._AffrmgPty

	@AffrmgPty.setter
	def AffrmgPty(self, value):
		self._AffrmgPty = value if type(value) != base_types.auto else self.make_default("AffrmgPty")

	@AffrmgPty.deleter
	def AffrmgPty(self):
		del self._AffrmgPty
		self._AffrmgPty = None

	@property
	def CMUCtrPty(self):
		return self._CMUCtrPty

	@CMUCtrPty.setter
	def CMUCtrPty(self, value):
		self._CMUCtrPty = value if type(value) != base_types.auto else self.make_default("CMUCtrPty")

	@CMUCtrPty.deleter
	def CMUCtrPty(self):
		del self._CMUCtrPty
		self._CMUCtrPty = None

	@property
	def ExctgBrkr(self):
		return self._ExctgBrkr

	@ExctgBrkr.setter
	def ExctgBrkr(self, value):
		self._ExctgBrkr = value if type(value) != base_types.auto else self.make_default("ExctgBrkr")

	@ExctgBrkr.deleter
	def ExctgBrkr(self):
		del self._ExctgBrkr
		self._ExctgBrkr = None

	@property
	def Lndr(self):
		return self._Lndr

	@Lndr.setter
	def Lndr(self, value):
		self._Lndr = value if type(value) != base_types.auto else self.make_default("Lndr")

	@Lndr.deleter
	def Lndr(self):
		del self._Lndr
		self._Lndr = None

	@property
	def Buyr(self):
		return self._Buyr

	@Buyr.setter
	def Buyr(self, value):
		self._Buyr = value if type(value) != base_types.auto else self.make_default("Buyr")

	@Buyr.deleter
	def Buyr(self):
		del self._Buyr
		self._Buyr = None

	@property
	def TradBnfcryPty(self):
		return self._TradBnfcryPty

	@TradBnfcryPty.setter
	def TradBnfcryPty(self, value):
		self._TradBnfcryPty = value if type(value) != base_types.auto else self.make_default("TradBnfcryPty")

	@TradBnfcryPty.deleter
	def TradBnfcryPty(self):
		del self._TradBnfcryPty
		self._TradBnfcryPty = None

	@property
	def StepInFirm(self):
		return self._StepInFirm

	@StepInFirm.setter
	def StepInFirm(self, value):
		self._StepInFirm = value if type(value) != base_types.auto else self.make_default("StepInFirm")

	@StepInFirm.deleter
	def StepInFirm(self):
		del self._StepInFirm
		self._StepInFirm = None

	@property
	def BrkrOfCdt(self):
		return self._BrkrOfCdt

	@BrkrOfCdt.setter
	def BrkrOfCdt(self, value):
		self._BrkrOfCdt = value if type(value) != base_types.auto else self.make_default("BrkrOfCdt")

	@BrkrOfCdt.deleter
	def BrkrOfCdt(self):
		del self._BrkrOfCdt
		self._BrkrOfCdt = None

	@property
	def IntrdcgFirm(self):
		return self._IntrdcgFirm

	@IntrdcgFirm.setter
	def IntrdcgFirm(self, value):
		self._IntrdcgFirm = value if type(value) != base_types.auto else self.make_default("IntrdcgFirm")

	@IntrdcgFirm.deleter
	def IntrdcgFirm(self):
		del self._IntrdcgFirm
		self._IntrdcgFirm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Brrwr', type=ConfirmationPartyDetails12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sellr', type=ConfirmationPartyDetails12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StepOutFirm', type=ConfirmationPartyDetails11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrFirm', type=ConfirmationPartyDetails13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CMUPty', type=ConfirmationPartyDetails11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AffrmgPty', type=ConfirmationPartyDetails11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CMUCtrPty', type=ConfirmationPartyDetails11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctgBrkr', type=ConfirmationPartyDetails13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lndr', type=ConfirmationPartyDetails12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Buyr', type=ConfirmationPartyDetails12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradBnfcryPty', type=ConfirmationPartyDetails14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StepInFirm', type=ConfirmationPartyDetails11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrkrOfCdt', type=ConfirmationPartyDetails11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrdcgFirm', type=ConfirmationPartyDetails11, min=0, max=1, mutex_group=None, array=False),
	))

