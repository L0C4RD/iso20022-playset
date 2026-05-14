# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from ._ISINOct2015Identifier import ISINOct2015Identifier
from ._ISODate import ISODate
from ._Max25Text import Max25Text
from ._Number import Number
from ._RestrictedMonthExact2Number import RestrictedMonthExact2Number

class CreditDefaultSwapIndex3(base_types._BaseFieldType):

	__slots__ = ["_NtnlCcy", "_NxtRollDt", "_RollMnth", "_Srs", "_UndrlygIndxId", "_UndrlygIndxNm", "_Vrsn"]
	@property
	def NtnlCcy(self):
		return self._NtnlCcy

	@NtnlCcy.setter
	def NtnlCcy(self, value):
		self._NtnlCcy = value if type(value) != base_types.auto else self.make_default("NtnlCcy")

	@NtnlCcy.deleter
	def NtnlCcy(self):
		del self._NtnlCcy
		self._NtnlCcy = None

	@property
	def NxtRollDt(self):
		return self._NxtRollDt

	@NxtRollDt.setter
	def NxtRollDt(self, value):
		self._NxtRollDt = value if type(value) != base_types.auto else self.make_default("NxtRollDt")

	@NxtRollDt.deleter
	def NxtRollDt(self):
		del self._NxtRollDt
		self._NxtRollDt = None

	@property
	def RollMnth(self):
		return self._RollMnth

	@RollMnth.setter
	def RollMnth(self, value):
		self._RollMnth = value if type(value) != base_types.auto else self.make_default("RollMnth")

	@RollMnth.deleter
	def RollMnth(self):
		del self._RollMnth
		self._RollMnth = None

	@property
	def Srs(self):
		return self._Srs

	@Srs.setter
	def Srs(self, value):
		self._Srs = value if type(value) != base_types.auto else self.make_default("Srs")

	@Srs.deleter
	def Srs(self):
		del self._Srs
		self._Srs = None

	@property
	def UndrlygIndxId(self):
		return self._UndrlygIndxId

	@UndrlygIndxId.setter
	def UndrlygIndxId(self, value):
		self._UndrlygIndxId = value if type(value) != base_types.auto else self.make_default("UndrlygIndxId")

	@UndrlygIndxId.deleter
	def UndrlygIndxId(self):
		del self._UndrlygIndxId
		self._UndrlygIndxId = None

	@property
	def UndrlygIndxNm(self):
		return self._UndrlygIndxNm

	@UndrlygIndxNm.setter
	def UndrlygIndxNm(self, value):
		self._UndrlygIndxNm = value if type(value) != base_types.auto else self.make_default("UndrlygIndxNm")

	@UndrlygIndxNm.deleter
	def UndrlygIndxNm(self):
		del self._UndrlygIndxNm
		self._UndrlygIndxNm = None

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if type(value) != base_types.auto else self.make_default("Vrsn")

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NtnlCcy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtRollDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RollMnth', type=RestrictedMonthExact2Number, min=0, max=12, mutex_group=None, array=True),
		base_types.FieldEntry(name='Srs', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygIndxId', type=ISINOct2015Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygIndxNm', type=Max25Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Number, min=0, max=1, mutex_group=None, array=False),
	))