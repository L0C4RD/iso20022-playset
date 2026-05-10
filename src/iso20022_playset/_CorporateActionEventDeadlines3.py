from . import base_types
from ._DateFormat44Choice import DateFormat44Choice
from ._DateFormat43Choice import DateFormat43Choice

class CorporateActionEventDeadlines3(base_types._BaseFieldType):

	__slots__ = ["_MktDdln", "_CoverPrtctDdln", "_PrtctDdln", "_EarlyRspnDdln", "_RspnDdln"]
	@property
	def CoverPrtctDdln(self):
		return self._CoverPrtctDdln

	@CoverPrtctDdln.setter
	def CoverPrtctDdln(self, value):
		self._CoverPrtctDdln = value if type(value) != base_types.auto else self.make_default("CoverPrtctDdln")

	@CoverPrtctDdln.deleter
	def CoverPrtctDdln(self):
		del self._CoverPrtctDdln
		self._CoverPrtctDdln = None

	@property
	def EarlyRspnDdln(self):
		return self._EarlyRspnDdln

	@EarlyRspnDdln.setter
	def EarlyRspnDdln(self, value):
		self._EarlyRspnDdln = value if type(value) != base_types.auto else self.make_default("EarlyRspnDdln")

	@EarlyRspnDdln.deleter
	def EarlyRspnDdln(self):
		del self._EarlyRspnDdln
		self._EarlyRspnDdln = None

	@property
	def MktDdln(self):
		return self._MktDdln

	@MktDdln.setter
	def MktDdln(self, value):
		self._MktDdln = value if type(value) != base_types.auto else self.make_default("MktDdln")

	@MktDdln.deleter
	def MktDdln(self):
		del self._MktDdln
		self._MktDdln = None

	@property
	def PrtctDdln(self):
		return self._PrtctDdln

	@PrtctDdln.setter
	def PrtctDdln(self, value):
		self._PrtctDdln = value if type(value) != base_types.auto else self.make_default("PrtctDdln")

	@PrtctDdln.deleter
	def PrtctDdln(self):
		del self._PrtctDdln
		self._PrtctDdln = None

	@property
	def RspnDdln(self):
		return self._RspnDdln

	@RspnDdln.setter
	def RspnDdln(self, value):
		self._RspnDdln = value if type(value) != base_types.auto else self.make_default("RspnDdln")

	@RspnDdln.deleter
	def RspnDdln(self):
		del self._RspnDdln
		self._RspnDdln = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CoverPrtctDdln', type=DateFormat43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlyRspnDdln', type=DateFormat43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktDdln', type=DateFormat43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctDdln', type=DateFormat43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnDdln', type=DateFormat44Choice, min=0, max=1, mutex_group=None, array=False),
	))

