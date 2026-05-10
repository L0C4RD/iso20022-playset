from . import base_types
import OptionEvent2
import ExoticOptionStyle1Code
import TrueFalseIndicator
import OptionType1Code
import OptionStyle5Code

class Option14(base_types._BaseFieldType):

	__slots__ = ["_OptnTp", "_OptnStyle", "_BrrrInd", "_XprtnStyle", "_EvtTp"]
	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if type(value) != auto else self.make_default("OptnTp")

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = None

	@property
	def OptnStyle(self):
		return self._OptnStyle

	@OptnStyle.setter
	def OptnStyle(self, value):
		self._OptnStyle = value if type(value) != auto else self.make_default("OptnStyle")

	@OptnStyle.deleter
	def OptnStyle(self):
		del self._OptnStyle
		self._OptnStyle = None

	@property
	def BrrrInd(self):
		return self._BrrrInd

	@BrrrInd.setter
	def BrrrInd(self, value):
		self._BrrrInd = value if type(value) != auto else self.make_default("BrrrInd")

	@BrrrInd.deleter
	def BrrrInd(self):
		del self._BrrrInd
		self._BrrrInd = None

	@property
	def XprtnStyle(self):
		return self._XprtnStyle

	@XprtnStyle.setter
	def XprtnStyle(self, value):
		self._XprtnStyle = value if type(value) != auto else self.make_default("XprtnStyle")

	@XprtnStyle.deleter
	def XprtnStyle(self):
		del self._XprtnStyle
		self._XprtnStyle = None

	@property
	def EvtTp(self):
		return self._EvtTp

	@EvtTp.setter
	def EvtTp(self, value):
		self._EvtTp = value if type(value) != auto else self.make_default("EvtTp")

	@EvtTp.deleter
	def EvtTp(self):
		del self._EvtTp
		self._EvtTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OptnTp', type=OptionType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnStyle', type=ExoticOptionStyle1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrrrInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XprtnStyle', type=OptionStyle5Code, min=1, max=4, mutex_group=None, array=True),
		base_types.FieldEntry(name='EvtTp', type=OptionEvent2, min=0, max=1, mutex_group=None, array=False),
	))

