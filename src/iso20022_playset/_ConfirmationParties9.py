# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ConfirmationPartyDetails11
from . import ConfirmationPartyDetails12
from . import ConfirmationPartyDetails14
from . import ConfirmationPartyDetails16
from . import PartyIdentificationAndAccount220

class ConfirmationParties9(base_types._BaseFieldType):

	__slots__ = ["_AffrmgPty", "_BrkrOfCdt", "_Brrwr", "_Buyr", "_ClrFirm", "_ExctgBrkr", "_IntrdcgFirm", "_Invstr", "_Lndr", "_Sellr", "_StepInFirm", "_StepOutFirm", "_TradBnfcryPty"]
	@property
	def AffrmgPty(self):
		return self._AffrmgPty

	@AffrmgPty.setter
	def AffrmgPty(self, value):
		self._AffrmgPty = value if value is not None else base_types.UninitialisedField(self, 'AffrmgPty', ConfirmationPartyDetails14, False)

	@AffrmgPty.deleter
	def AffrmgPty(self):
		del self._AffrmgPty
		self._AffrmgPty = base_types.UninitialisedField(self, 'AffrmgPty', ConfirmationPartyDetails14, False)

	@property
	def BrkrOfCdt(self):
		return self._BrkrOfCdt

	@BrkrOfCdt.setter
	def BrkrOfCdt(self, value):
		self._BrkrOfCdt = value if value is not None else base_types.UninitialisedField(self, 'BrkrOfCdt', ConfirmationPartyDetails14, False)

	@BrkrOfCdt.deleter
	def BrkrOfCdt(self):
		del self._BrkrOfCdt
		self._BrkrOfCdt = base_types.UninitialisedField(self, 'BrkrOfCdt', ConfirmationPartyDetails14, False)

	@property
	def Brrwr(self):
		return self._Brrwr

	@Brrwr.setter
	def Brrwr(self, value):
		self._Brrwr = value if value is not None else base_types.UninitialisedField(self, 'Brrwr', ConfirmationPartyDetails12, False)

	@Brrwr.deleter
	def Brrwr(self):
		del self._Brrwr
		self._Brrwr = base_types.UninitialisedField(self, 'Brrwr', ConfirmationPartyDetails12, False)

	@property
	def Buyr(self):
		return self._Buyr

	@Buyr.setter
	def Buyr(self, value):
		self._Buyr = value if value is not None else base_types.UninitialisedField(self, 'Buyr', ConfirmationPartyDetails12, False)

	@Buyr.deleter
	def Buyr(self):
		del self._Buyr
		self._Buyr = base_types.UninitialisedField(self, 'Buyr', ConfirmationPartyDetails12, False)

	@property
	def ClrFirm(self):
		return self._ClrFirm

	@ClrFirm.setter
	def ClrFirm(self, value):
		self._ClrFirm = value if value is not None else base_types.UninitialisedField(self, 'ClrFirm', ConfirmationPartyDetails16, False)

	@ClrFirm.deleter
	def ClrFirm(self):
		del self._ClrFirm
		self._ClrFirm = base_types.UninitialisedField(self, 'ClrFirm', ConfirmationPartyDetails16, False)

	@property
	def ExctgBrkr(self):
		return self._ExctgBrkr

	@ExctgBrkr.setter
	def ExctgBrkr(self, value):
		self._ExctgBrkr = value if value is not None else base_types.UninitialisedField(self, 'ExctgBrkr', ConfirmationPartyDetails16, False)

	@ExctgBrkr.deleter
	def ExctgBrkr(self):
		del self._ExctgBrkr
		self._ExctgBrkr = base_types.UninitialisedField(self, 'ExctgBrkr', ConfirmationPartyDetails16, False)

	@property
	def IntrdcgFirm(self):
		return self._IntrdcgFirm

	@IntrdcgFirm.setter
	def IntrdcgFirm(self, value):
		self._IntrdcgFirm = value if value is not None else base_types.UninitialisedField(self, 'IntrdcgFirm', ConfirmationPartyDetails14, False)

	@IntrdcgFirm.deleter
	def IntrdcgFirm(self):
		del self._IntrdcgFirm
		self._IntrdcgFirm = base_types.UninitialisedField(self, 'IntrdcgFirm', ConfirmationPartyDetails14, False)

	@property
	def Invstr(self):
		return self._Invstr

	@Invstr.setter
	def Invstr(self, value):
		self._Invstr = value if value is not None else base_types.UninitialisedField(self, 'Invstr', PartyIdentificationAndAccount220, True)

	@Invstr.deleter
	def Invstr(self):
		del self._Invstr
		self._Invstr = base_types.UninitialisedField(self, 'Invstr', PartyIdentificationAndAccount220, True)

	@property
	def Lndr(self):
		return self._Lndr

	@Lndr.setter
	def Lndr(self, value):
		self._Lndr = value if value is not None else base_types.UninitialisedField(self, 'Lndr', ConfirmationPartyDetails12, False)

	@Lndr.deleter
	def Lndr(self):
		del self._Lndr
		self._Lndr = base_types.UninitialisedField(self, 'Lndr', ConfirmationPartyDetails12, False)

	@property
	def Sellr(self):
		return self._Sellr

	@Sellr.setter
	def Sellr(self, value):
		self._Sellr = value if value is not None else base_types.UninitialisedField(self, 'Sellr', ConfirmationPartyDetails12, False)

	@Sellr.deleter
	def Sellr(self):
		del self._Sellr
		self._Sellr = base_types.UninitialisedField(self, 'Sellr', ConfirmationPartyDetails12, False)

	@property
	def StepInFirm(self):
		return self._StepInFirm

	@StepInFirm.setter
	def StepInFirm(self, value):
		self._StepInFirm = value if value is not None else base_types.UninitialisedField(self, 'StepInFirm', ConfirmationPartyDetails11, False)

	@StepInFirm.deleter
	def StepInFirm(self):
		del self._StepInFirm
		self._StepInFirm = base_types.UninitialisedField(self, 'StepInFirm', ConfirmationPartyDetails11, False)

	@property
	def StepOutFirm(self):
		return self._StepOutFirm

	@StepOutFirm.setter
	def StepOutFirm(self, value):
		self._StepOutFirm = value if value is not None else base_types.UninitialisedField(self, 'StepOutFirm', ConfirmationPartyDetails11, False)

	@StepOutFirm.deleter
	def StepOutFirm(self):
		del self._StepOutFirm
		self._StepOutFirm = base_types.UninitialisedField(self, 'StepOutFirm', ConfirmationPartyDetails11, False)

	@property
	def TradBnfcryPty(self):
		return self._TradBnfcryPty

	@TradBnfcryPty.setter
	def TradBnfcryPty(self, value):
		self._TradBnfcryPty = value if value is not None else base_types.UninitialisedField(self, 'TradBnfcryPty', ConfirmationPartyDetails14, False)

	@TradBnfcryPty.deleter
	def TradBnfcryPty(self):
		del self._TradBnfcryPty
		self._TradBnfcryPty = base_types.UninitialisedField(self, 'TradBnfcryPty', ConfirmationPartyDetails14, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AffrmgPty', type=ConfirmationPartyDetails14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrkrOfCdt', type=ConfirmationPartyDetails14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Brrwr', type=ConfirmationPartyDetails12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Buyr', type=ConfirmationPartyDetails12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrFirm', type=ConfirmationPartyDetails16, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctgBrkr', type=ConfirmationPartyDetails16, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrdcgFirm', type=ConfirmationPartyDetails14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Invstr', type=PartyIdentificationAndAccount220, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Lndr', type=ConfirmationPartyDetails12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sellr', type=ConfirmationPartyDetails12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StepInFirm', type=ConfirmationPartyDetails11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StepOutFirm', type=ConfirmationPartyDetails11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradBnfcryPty', type=ConfirmationPartyDetails14, min=0, max=1, mutex_group=None, array=False),
	))