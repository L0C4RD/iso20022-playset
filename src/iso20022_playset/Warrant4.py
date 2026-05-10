import base_types
import BaseOneRate
import Organisation38
import Price8
import WarrantStyle3Choice

class Warrant4(base_types._BaseFieldType):

	__slots__ = ["_WarrtAgt", "_Tp", "_SbcptPric", "_Mltplr"]
	@property
	def WarrtAgt(self):
		return self._WarrtAgt

	@WarrtAgt.setter
	def WarrtAgt(self, value):
		self._WarrtAgt = value if type(value) != auto else self.make_default("WarrtAgt")

	@WarrtAgt.deleter
	def WarrtAgt(self):
		del self._WarrtAgt
		self._WarrtAgt = None

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
	def SbcptPric(self):
		return self._SbcptPric

	@SbcptPric.setter
	def SbcptPric(self, value):
		self._SbcptPric = value if type(value) != auto else self.make_default("SbcptPric")

	@SbcptPric.deleter
	def SbcptPric(self):
		del self._SbcptPric
		self._SbcptPric = None

	@property
	def Mltplr(self):
		return self._Mltplr

	@Mltplr.setter
	def Mltplr(self, value):
		self._Mltplr = value if type(value) != auto else self.make_default("Mltplr")

	@Mltplr.deleter
	def Mltplr(self):
		del self._Mltplr
		self._Mltplr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='WarrtAgt', type=Organisation38, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=WarrantStyle3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbcptPric', type=Price8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mltplr', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
	))

