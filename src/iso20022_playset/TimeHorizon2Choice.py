from . import base_types
from .DecimalNumber import DecimalNumber
from .TimeFrame9Choice import TimeFrame9Choice

class TimeHorizon2Choice(base_types._BaseFieldType):

	__slots__ = ["_NbOfYrs", "_TmFrame"]
	@property
	def NbOfYrs(self):
		return self._NbOfYrs

	@NbOfYrs.setter
	def NbOfYrs(self, value):
		self._NbOfYrs = value if type(value) != base_types.auto else self.make_default("NbOfYrs")

	@NbOfYrs.deleter
	def NbOfYrs(self):
		del self._NbOfYrs
		self._NbOfYrs = None

	@property
	def TmFrame(self):
		return self._TmFrame

	@TmFrame.setter
	def TmFrame(self, value):
		self._TmFrame = value if type(value) != base_types.auto else self.make_default("TmFrame")

	@TmFrame.deleter
	def TmFrame(self):
		del self._TmFrame
		self._TmFrame = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfYrs', type=DecimalNumber, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TmFrame', type=TimeFrame9Choice, min=0, max=1, mutex_group=1, array=False),
	))

