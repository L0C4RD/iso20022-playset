from . import base_types
from .Max35Text import Max35Text

class MultimodalTransport3(base_types._BaseFieldType):

	__slots__ = ["_PlcOfFnlDstn", "_TakngInChrg"]
	@property
	def PlcOfFnlDstn(self):
		return self._PlcOfFnlDstn

	@PlcOfFnlDstn.setter
	def PlcOfFnlDstn(self, value):
		self._PlcOfFnlDstn = value if type(value) != auto else self.make_default("PlcOfFnlDstn")

	@PlcOfFnlDstn.deleter
	def PlcOfFnlDstn(self):
		del self._PlcOfFnlDstn
		self._PlcOfFnlDstn = None

	@property
	def TakngInChrg(self):
		return self._TakngInChrg

	@TakngInChrg.setter
	def TakngInChrg(self, value):
		self._TakngInChrg = value if type(value) != auto else self.make_default("TakngInChrg")

	@TakngInChrg.deleter
	def TakngInChrg(self):
		del self._TakngInChrg
		self._TakngInChrg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PlcOfFnlDstn', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TakngInChrg', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

