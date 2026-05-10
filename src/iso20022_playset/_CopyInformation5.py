from . import base_types
from ._AnyBICDec2014Identifier import AnyBICDec2014Identifier
from ._YesNoIndicator import YesNoIndicator

class CopyInformation5(base_types._BaseFieldType):

	__slots__ = ["_CpyInd", "_OrgnlRcvr"]
	@property
	def CpyInd(self):
		return self._CpyInd

	@CpyInd.setter
	def CpyInd(self, value):
		self._CpyInd = value if type(value) != base_types.auto else self.make_default("CpyInd")

	@CpyInd.deleter
	def CpyInd(self):
		del self._CpyInd
		self._CpyInd = None

	@property
	def OrgnlRcvr(self):
		return self._OrgnlRcvr

	@OrgnlRcvr.setter
	def OrgnlRcvr(self, value):
		self._OrgnlRcvr = value if type(value) != base_types.auto else self.make_default("OrgnlRcvr")

	@OrgnlRcvr.deleter
	def OrgnlRcvr(self):
		del self._OrgnlRcvr
		self._OrgnlRcvr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CpyInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlRcvr', type=AnyBICDec2014Identifier, min=0, max=1, mutex_group=None, array=False),
	))

