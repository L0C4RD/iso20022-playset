from . import base_types
from ._PartyIdentification177Choice import PartyIdentification177Choice
from ._CardAccountType3Code import CardAccountType3Code
from ._Max70Text import Max70Text
from ._Max35Text import Max35Text
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._AmountAndDirection111 import AmountAndDirection111
from ._AccountIdentification80Choice import AccountIdentification80Choice

class CardAccount19(base_types._BaseFieldType):

	__slots__ = ["_BalAftr", "_CdtRef", "_AcctTp", "_Svcr", "_AcctNm", "_BalBfr", "_AcctIdr", "_Ccy"]
	@property
	def BalAftr(self):
		return self._BalAftr

	@BalAftr.setter
	def BalAftr(self, value):
		self._BalAftr = value if type(value) != base_types.auto else self.make_default("BalAftr")

	@BalAftr.deleter
	def BalAftr(self):
		del self._BalAftr
		self._BalAftr = None

	@property
	def CdtRef(self):
		return self._CdtRef

	@CdtRef.setter
	def CdtRef(self, value):
		self._CdtRef = value if type(value) != base_types.auto else self.make_default("CdtRef")

	@CdtRef.deleter
	def CdtRef(self):
		del self._CdtRef
		self._CdtRef = None

	@property
	def AcctTp(self):
		return self._AcctTp

	@AcctTp.setter
	def AcctTp(self, value):
		self._AcctTp = value if type(value) != base_types.auto else self.make_default("AcctTp")

	@AcctTp.deleter
	def AcctTp(self):
		del self._AcctTp
		self._AcctTp = None

	@property
	def Svcr(self):
		return self._Svcr

	@Svcr.setter
	def Svcr(self, value):
		self._Svcr = value if type(value) != base_types.auto else self.make_default("Svcr")

	@Svcr.deleter
	def Svcr(self):
		del self._Svcr
		self._Svcr = None

	@property
	def AcctNm(self):
		return self._AcctNm

	@AcctNm.setter
	def AcctNm(self, value):
		self._AcctNm = value if type(value) != base_types.auto else self.make_default("AcctNm")

	@AcctNm.deleter
	def AcctNm(self):
		del self._AcctNm
		self._AcctNm = None

	@property
	def BalBfr(self):
		return self._BalBfr

	@BalBfr.setter
	def BalBfr(self, value):
		self._BalBfr = value if type(value) != base_types.auto else self.make_default("BalBfr")

	@BalBfr.deleter
	def BalBfr(self):
		del self._BalBfr
		self._BalBfr = None

	@property
	def AcctIdr(self):
		return self._AcctIdr

	@AcctIdr.setter
	def AcctIdr(self, value):
		self._AcctIdr = value if type(value) != base_types.auto else self.make_default("AcctIdr")

	@AcctIdr.deleter
	def AcctIdr(self):
		del self._AcctIdr
		self._AcctIdr = None

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != base_types.auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BalAftr', type=AmountAndDirection111, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctTp', type=CardAccountType3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Svcr', type=PartyIdentification177Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalBfr', type=AmountAndDirection111, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctIdr', type=AccountIdentification80Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
	))

