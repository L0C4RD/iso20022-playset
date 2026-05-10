import base_types
import Max350Text
import Modification1Code

class TradingNameModification1(base_types._BaseFieldType):

	__slots__ = ["_TradgNm", "_ModCd"]
	@property
	def TradgNm(self):
		return self._TradgNm

	@TradgNm.setter
	def TradgNm(self, value):
		self._TradgNm = value if type(value) != auto else self.make_default("TradgNm")

	@TradgNm.deleter
	def TradgNm(self):
		del self._TradgNm
		self._TradgNm = None

	@property
	def ModCd(self):
		return self._ModCd

	@ModCd.setter
	def ModCd(self, value):
		self._ModCd = value if type(value) != auto else self.make_default("ModCd")

	@ModCd.deleter
	def ModCd(self):
		del self._ModCd
		self._ModCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TradgNm', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModCd', type=Modification1Code, min=0, max=1, mutex_group=None, array=False),
	))

