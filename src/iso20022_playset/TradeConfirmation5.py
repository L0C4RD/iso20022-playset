import base_types
import TradeConfirmationType1Code
import ISODateTime

class TradeConfirmation5(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_TmStmp"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def TmStmp(self):
		return self._TmStmp

	@TmStmp.setter
	def TmStmp(self, value):
		self._TmStmp = value if type(value) != auto else self.make_default("TmStmp")

	@TmStmp.deleter
	def TmStmp(self):
		del self._TmStmp
		self._TmStmp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=TradeConfirmationType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmStmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))

