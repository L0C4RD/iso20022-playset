from . import base_types
import Max35Text
import CurrencyExchangeSearchCriteria1

class CurrencyExchangeCriteria2(base_types._BaseFieldType):

	__slots__ = ["_NewQryNm", "_SchCrit"]
	@property
	def NewQryNm(self):
		return self._NewQryNm

	@NewQryNm.setter
	def NewQryNm(self, value):
		self._NewQryNm = value if type(value) != auto else self.make_default("NewQryNm")

	@NewQryNm.deleter
	def NewQryNm(self):
		del self._NewQryNm
		self._NewQryNm = None

	@property
	def SchCrit(self):
		return self._SchCrit

	@SchCrit.setter
	def SchCrit(self, value):
		self._SchCrit = value if type(value) != auto else self.make_default("SchCrit")

	@SchCrit.deleter
	def SchCrit(self):
		del self._SchCrit
		self._SchCrit = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NewQryNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SchCrit', type=CurrencyExchangeSearchCriteria1, min=1, max=None, mutex_group=None, array=True),
	))

