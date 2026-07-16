# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import ISODateTime
from . import LEIIdentifier
from . import Max350Text
from . import Max35Text
from . import PartyIdentification125Choice

class ThirdPartyRights2(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Desc", "_DtTm", "_Hldr", "_LglNttyIdr", "_Tp"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max350Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max350Text, False)

	@property
	def DtTm(self):
		return self._DtTm

	@DtTm.setter
	def DtTm(self, value):
		self._DtTm = value if value is not None else base_types.UninitialisedField(self, 'DtTm', ISODateTime, False)

	@DtTm.deleter
	def DtTm(self):
		del self._DtTm
		self._DtTm = base_types.UninitialisedField(self, 'DtTm', ISODateTime, False)

	@property
	def Hldr(self):
		return self._Hldr

	@Hldr.setter
	def Hldr(self, value):
		self._Hldr = value if value is not None else base_types.UninitialisedField(self, 'Hldr', PartyIdentification125Choice, False)

	@Hldr.deleter
	def Hldr(self):
		del self._Hldr
		self._Hldr = base_types.UninitialisedField(self, 'Hldr', PartyIdentification125Choice, False)

	@property
	def LglNttyIdr(self):
		return self._LglNttyIdr

	@LglNttyIdr.setter
	def LglNttyIdr(self, value):
		self._LglNttyIdr = value if value is not None else base_types.UninitialisedField(self, 'LglNttyIdr', LEIIdentifier, False)

	@LglNttyIdr.deleter
	def LglNttyIdr(self):
		del self._LglNttyIdr
		self._LglNttyIdr = base_types.UninitialisedField(self, 'LglNttyIdr', LEIIdentifier, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', Max35Text, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hldr', type=PartyIdentification125Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglNttyIdr', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))