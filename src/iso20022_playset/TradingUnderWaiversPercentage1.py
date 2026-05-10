import base_types
import PercentageRate
import Max350Text
import MICIdentifier

class TradingUnderWaiversPercentage1(base_types._BaseFieldType):

	__slots__ = ["_Dsclmr", "_TradgVn", "_TradgUdrWvrPctg"]
	@property
	def Dsclmr(self):
		return self._Dsclmr

	@Dsclmr.setter
	def Dsclmr(self, value):
		self._Dsclmr = value if type(value) != auto else self.make_default("Dsclmr")

	@Dsclmr.deleter
	def Dsclmr(self):
		del self._Dsclmr
		self._Dsclmr = None

	@property
	def TradgVn(self):
		return self._TradgVn

	@TradgVn.setter
	def TradgVn(self, value):
		self._TradgVn = value if type(value) != auto else self.make_default("TradgVn")

	@TradgVn.deleter
	def TradgVn(self):
		del self._TradgVn
		self._TradgVn = None

	@property
	def TradgUdrWvrPctg(self):
		return self._TradgUdrWvrPctg

	@TradgUdrWvrPctg.setter
	def TradgUdrWvrPctg(self, value):
		self._TradgUdrWvrPctg = value if type(value) != auto else self.make_default("TradgUdrWvrPctg")

	@TradgUdrWvrPctg.deleter
	def TradgUdrWvrPctg(self):
		del self._TradgUdrWvrPctg
		self._TradgUdrWvrPctg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dsclmr', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgVn', type=MICIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgUdrWvrPctg', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
	))

