# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DebtInstrumentSeniorityType2Code
from . import DerivativePartyIdentification1Choice
from . import Frequency13Code
from . import Max35Text
from . import Number
from . import PercentageRate
from . import TrueFalseIndicator

class CreditDerivative7(base_types._BaseFieldType):

	__slots__ = ["_ClctnBsis", "_IndxFctr", "_PmtFrqcy", "_RefPty", "_Snrty", "_Srs", "_TrchInd", "_Vrsn"]
	@property
	def ClctnBsis(self):
		return self._ClctnBsis

	@ClctnBsis.setter
	def ClctnBsis(self, value):
		self._ClctnBsis = value if value is not None else base_types.UninitialisedField(self, 'ClctnBsis', Max35Text, False)

	@ClctnBsis.deleter
	def ClctnBsis(self):
		del self._ClctnBsis
		self._ClctnBsis = base_types.UninitialisedField(self, 'ClctnBsis', Max35Text, False)

	@property
	def IndxFctr(self):
		return self._IndxFctr

	@IndxFctr.setter
	def IndxFctr(self, value):
		self._IndxFctr = value if value is not None else base_types.UninitialisedField(self, 'IndxFctr', PercentageRate, False)

	@IndxFctr.deleter
	def IndxFctr(self):
		del self._IndxFctr
		self._IndxFctr = base_types.UninitialisedField(self, 'IndxFctr', PercentageRate, False)

	@property
	def PmtFrqcy(self):
		return self._PmtFrqcy

	@PmtFrqcy.setter
	def PmtFrqcy(self, value):
		self._PmtFrqcy = value if value is not None else base_types.UninitialisedField(self, 'PmtFrqcy', Frequency13Code, False)

	@PmtFrqcy.deleter
	def PmtFrqcy(self):
		del self._PmtFrqcy
		self._PmtFrqcy = base_types.UninitialisedField(self, 'PmtFrqcy', Frequency13Code, False)

	@property
	def RefPty(self):
		return self._RefPty

	@RefPty.setter
	def RefPty(self, value):
		self._RefPty = value if value is not None else base_types.UninitialisedField(self, 'RefPty', DerivativePartyIdentification1Choice, False)

	@RefPty.deleter
	def RefPty(self):
		del self._RefPty
		self._RefPty = base_types.UninitialisedField(self, 'RefPty', DerivativePartyIdentification1Choice, False)

	@property
	def Snrty(self):
		return self._Snrty

	@Snrty.setter
	def Snrty(self, value):
		self._Snrty = value if value is not None else base_types.UninitialisedField(self, 'Snrty', DebtInstrumentSeniorityType2Code, False)

	@Snrty.deleter
	def Snrty(self):
		del self._Snrty
		self._Snrty = base_types.UninitialisedField(self, 'Snrty', DebtInstrumentSeniorityType2Code, False)

	@property
	def Srs(self):
		return self._Srs

	@Srs.setter
	def Srs(self, value):
		self._Srs = value if value is not None else base_types.UninitialisedField(self, 'Srs', Number, False)

	@Srs.deleter
	def Srs(self):
		del self._Srs
		self._Srs = base_types.UninitialisedField(self, 'Srs', Number, False)

	@property
	def TrchInd(self):
		return self._TrchInd

	@TrchInd.setter
	def TrchInd(self, value):
		self._TrchInd = value if value is not None else base_types.UninitialisedField(self, 'TrchInd', TrueFalseIndicator, False)

	@TrchInd.deleter
	def TrchInd(self):
		del self._TrchInd
		self._TrchInd = base_types.UninitialisedField(self, 'TrchInd', TrueFalseIndicator, False)

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if value is not None else base_types.UninitialisedField(self, 'Vrsn', Number, False)

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = base_types.UninitialisedField(self, 'Vrsn', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClctnBsis', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndxFctr', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtFrqcy', type=Frequency13Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefPty', type=DerivativePartyIdentification1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Snrty', type=DebtInstrumentSeniorityType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Srs', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrchInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Number, min=0, max=1, mutex_group=None, array=False),
	))