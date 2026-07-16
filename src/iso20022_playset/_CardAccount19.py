# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentification80Choice
from . import ActiveCurrencyCode
from . import AmountAndDirection111
from . import CardAccountType3Code
from . import Max35Text
from . import Max70Text
from . import PartyIdentification177Choice

class CardAccount19(base_types._BaseFieldType):

	__slots__ = ["_AcctIdr", "_AcctNm", "_AcctTp", "_BalAftr", "_BalBfr", "_Ccy", "_CdtRef", "_Svcr"]
	@property
	def AcctIdr(self):
		return self._AcctIdr

	@AcctIdr.setter
	def AcctIdr(self, value):
		self._AcctIdr = value if value is not None else base_types.UninitialisedField(self, 'AcctIdr', AccountIdentification80Choice, False)

	@AcctIdr.deleter
	def AcctIdr(self):
		del self._AcctIdr
		self._AcctIdr = base_types.UninitialisedField(self, 'AcctIdr', AccountIdentification80Choice, False)

	@property
	def AcctNm(self):
		return self._AcctNm

	@AcctNm.setter
	def AcctNm(self, value):
		self._AcctNm = value if value is not None else base_types.UninitialisedField(self, 'AcctNm', Max70Text, False)

	@AcctNm.deleter
	def AcctNm(self):
		del self._AcctNm
		self._AcctNm = base_types.UninitialisedField(self, 'AcctNm', Max70Text, False)

	@property
	def AcctTp(self):
		return self._AcctTp

	@AcctTp.setter
	def AcctTp(self, value):
		self._AcctTp = value if value is not None else base_types.UninitialisedField(self, 'AcctTp', CardAccountType3Code, False)

	@AcctTp.deleter
	def AcctTp(self):
		del self._AcctTp
		self._AcctTp = base_types.UninitialisedField(self, 'AcctTp', CardAccountType3Code, False)

	@property
	def BalAftr(self):
		return self._BalAftr

	@BalAftr.setter
	def BalAftr(self, value):
		self._BalAftr = value if value is not None else base_types.UninitialisedField(self, 'BalAftr', AmountAndDirection111, False)

	@BalAftr.deleter
	def BalAftr(self):
		del self._BalAftr
		self._BalAftr = base_types.UninitialisedField(self, 'BalAftr', AmountAndDirection111, False)

	@property
	def BalBfr(self):
		return self._BalBfr

	@BalBfr.setter
	def BalBfr(self, value):
		self._BalBfr = value if value is not None else base_types.UninitialisedField(self, 'BalBfr', AmountAndDirection111, False)

	@BalBfr.deleter
	def BalBfr(self):
		del self._BalBfr
		self._BalBfr = base_types.UninitialisedField(self, 'BalBfr', AmountAndDirection111, False)

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@property
	def CdtRef(self):
		return self._CdtRef

	@CdtRef.setter
	def CdtRef(self, value):
		self._CdtRef = value if value is not None else base_types.UninitialisedField(self, 'CdtRef', Max35Text, False)

	@CdtRef.deleter
	def CdtRef(self):
		del self._CdtRef
		self._CdtRef = base_types.UninitialisedField(self, 'CdtRef', Max35Text, False)

	@property
	def Svcr(self):
		return self._Svcr

	@Svcr.setter
	def Svcr(self, value):
		self._Svcr = value if value is not None else base_types.UninitialisedField(self, 'Svcr', PartyIdentification177Choice, False)

	@Svcr.deleter
	def Svcr(self):
		del self._Svcr
		self._Svcr = base_types.UninitialisedField(self, 'Svcr', PartyIdentification177Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctIdr', type=AccountIdentification80Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctTp', type=CardAccountType3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalAftr', type=AmountAndDirection111, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalBfr', type=AmountAndDirection111, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Svcr', type=PartyIdentification177Choice, min=0, max=1, mutex_group=None, array=False),
	))