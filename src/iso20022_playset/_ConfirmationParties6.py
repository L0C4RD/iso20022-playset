# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ConfirmationPartyDetails10
from . import ConfirmationPartyDetails7
from . import ConfirmationPartyDetails8
from . import ConfirmationPartyDetails9

class ConfirmationParties6(base_types._BaseFieldType):

	__slots__ = ["_AffrmgPty", "_BrkrOfCdt", "_Brrwr", "_Buyr", "_CMUCtrPty", "_CMUPty", "_ClrFirm", "_ExctgBrkr", "_IntrdcgFirm", "_Lndr", "_Sellr", "_StepInFirm", "_StepOutFirm", "_TradBnfcryPty"]
	@property
	def AffrmgPty(self):
		return self._AffrmgPty

	@AffrmgPty.setter
	def AffrmgPty(self, value):
		self._AffrmgPty = value if value is not None else base_types.UninitialisedField(self, 'AffrmgPty', ConfirmationPartyDetails8, False)

	@AffrmgPty.deleter
	def AffrmgPty(self):
		del self._AffrmgPty
		self._AffrmgPty = base_types.UninitialisedField(self, 'AffrmgPty', ConfirmationPartyDetails8, False)

	@property
	def BrkrOfCdt(self):
		return self._BrkrOfCdt

	@BrkrOfCdt.setter
	def BrkrOfCdt(self, value):
		self._BrkrOfCdt = value if value is not None else base_types.UninitialisedField(self, 'BrkrOfCdt', ConfirmationPartyDetails8, False)

	@BrkrOfCdt.deleter
	def BrkrOfCdt(self):
		del self._BrkrOfCdt
		self._BrkrOfCdt = base_types.UninitialisedField(self, 'BrkrOfCdt', ConfirmationPartyDetails8, False)

	@property
	def Brrwr(self):
		return self._Brrwr

	@Brrwr.setter
	def Brrwr(self, value):
		self._Brrwr = value if value is not None else base_types.UninitialisedField(self, 'Brrwr', ConfirmationPartyDetails7, False)

	@Brrwr.deleter
	def Brrwr(self):
		del self._Brrwr
		self._Brrwr = base_types.UninitialisedField(self, 'Brrwr', ConfirmationPartyDetails7, False)

	@property
	def Buyr(self):
		return self._Buyr

	@Buyr.setter
	def Buyr(self, value):
		self._Buyr = value if value is not None else base_types.UninitialisedField(self, 'Buyr', ConfirmationPartyDetails7, False)

	@Buyr.deleter
	def Buyr(self):
		del self._Buyr
		self._Buyr = base_types.UninitialisedField(self, 'Buyr', ConfirmationPartyDetails7, False)

	@property
	def CMUCtrPty(self):
		return self._CMUCtrPty

	@CMUCtrPty.setter
	def CMUCtrPty(self, value):
		self._CMUCtrPty = value if value is not None else base_types.UninitialisedField(self, 'CMUCtrPty', ConfirmationPartyDetails8, False)

	@CMUCtrPty.deleter
	def CMUCtrPty(self):
		del self._CMUCtrPty
		self._CMUCtrPty = base_types.UninitialisedField(self, 'CMUCtrPty', ConfirmationPartyDetails8, False)

	@property
	def CMUPty(self):
		return self._CMUPty

	@CMUPty.setter
	def CMUPty(self, value):
		self._CMUPty = value if value is not None else base_types.UninitialisedField(self, 'CMUPty', ConfirmationPartyDetails8, False)

	@CMUPty.deleter
	def CMUPty(self):
		del self._CMUPty
		self._CMUPty = base_types.UninitialisedField(self, 'CMUPty', ConfirmationPartyDetails8, False)

	@property
	def ClrFirm(self):
		return self._ClrFirm

	@ClrFirm.setter
	def ClrFirm(self, value):
		self._ClrFirm = value if value is not None else base_types.UninitialisedField(self, 'ClrFirm', ConfirmationPartyDetails9, False)

	@ClrFirm.deleter
	def ClrFirm(self):
		del self._ClrFirm
		self._ClrFirm = base_types.UninitialisedField(self, 'ClrFirm', ConfirmationPartyDetails9, False)

	@property
	def ExctgBrkr(self):
		return self._ExctgBrkr

	@ExctgBrkr.setter
	def ExctgBrkr(self, value):
		self._ExctgBrkr = value if value is not None else base_types.UninitialisedField(self, 'ExctgBrkr', ConfirmationPartyDetails9, False)

	@ExctgBrkr.deleter
	def ExctgBrkr(self):
		del self._ExctgBrkr
		self._ExctgBrkr = base_types.UninitialisedField(self, 'ExctgBrkr', ConfirmationPartyDetails9, False)

	@property
	def IntrdcgFirm(self):
		return self._IntrdcgFirm

	@IntrdcgFirm.setter
	def IntrdcgFirm(self, value):
		self._IntrdcgFirm = value if value is not None else base_types.UninitialisedField(self, 'IntrdcgFirm', ConfirmationPartyDetails8, False)

	@IntrdcgFirm.deleter
	def IntrdcgFirm(self):
		del self._IntrdcgFirm
		self._IntrdcgFirm = base_types.UninitialisedField(self, 'IntrdcgFirm', ConfirmationPartyDetails8, False)

	@property
	def Lndr(self):
		return self._Lndr

	@Lndr.setter
	def Lndr(self, value):
		self._Lndr = value if value is not None else base_types.UninitialisedField(self, 'Lndr', ConfirmationPartyDetails7, False)

	@Lndr.deleter
	def Lndr(self):
		del self._Lndr
		self._Lndr = base_types.UninitialisedField(self, 'Lndr', ConfirmationPartyDetails7, False)

	@property
	def Sellr(self):
		return self._Sellr

	@Sellr.setter
	def Sellr(self, value):
		self._Sellr = value if value is not None else base_types.UninitialisedField(self, 'Sellr', ConfirmationPartyDetails7, False)

	@Sellr.deleter
	def Sellr(self):
		del self._Sellr
		self._Sellr = base_types.UninitialisedField(self, 'Sellr', ConfirmationPartyDetails7, False)

	@property
	def StepInFirm(self):
		return self._StepInFirm

	@StepInFirm.setter
	def StepInFirm(self, value):
		self._StepInFirm = value if value is not None else base_types.UninitialisedField(self, 'StepInFirm', ConfirmationPartyDetails8, False)

	@StepInFirm.deleter
	def StepInFirm(self):
		del self._StepInFirm
		self._StepInFirm = base_types.UninitialisedField(self, 'StepInFirm', ConfirmationPartyDetails8, False)

	@property
	def StepOutFirm(self):
		return self._StepOutFirm

	@StepOutFirm.setter
	def StepOutFirm(self, value):
		self._StepOutFirm = value if value is not None else base_types.UninitialisedField(self, 'StepOutFirm', ConfirmationPartyDetails8, False)

	@StepOutFirm.deleter
	def StepOutFirm(self):
		del self._StepOutFirm
		self._StepOutFirm = base_types.UninitialisedField(self, 'StepOutFirm', ConfirmationPartyDetails8, False)

	@property
	def TradBnfcryPty(self):
		return self._TradBnfcryPty

	@TradBnfcryPty.setter
	def TradBnfcryPty(self, value):
		self._TradBnfcryPty = value if value is not None else base_types.UninitialisedField(self, 'TradBnfcryPty', ConfirmationPartyDetails10, False)

	@TradBnfcryPty.deleter
	def TradBnfcryPty(self):
		del self._TradBnfcryPty
		self._TradBnfcryPty = base_types.UninitialisedField(self, 'TradBnfcryPty', ConfirmationPartyDetails10, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AffrmgPty', type=ConfirmationPartyDetails8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrkrOfCdt', type=ConfirmationPartyDetails8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Brrwr', type=ConfirmationPartyDetails7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Buyr', type=ConfirmationPartyDetails7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CMUCtrPty', type=ConfirmationPartyDetails8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CMUPty', type=ConfirmationPartyDetails8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrFirm', type=ConfirmationPartyDetails9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctgBrkr', type=ConfirmationPartyDetails9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrdcgFirm', type=ConfirmationPartyDetails8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lndr', type=ConfirmationPartyDetails7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sellr', type=ConfirmationPartyDetails7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StepInFirm', type=ConfirmationPartyDetails8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StepOutFirm', type=ConfirmationPartyDetails8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradBnfcryPty', type=ConfirmationPartyDetails10, min=0, max=1, mutex_group=None, array=False),
	))