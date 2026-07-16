# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ExoticOptionStyle1Code
from . import OptionEvent2
from . import OptionStyle5Code
from . import OptionType1Code
from . import TrueFalseIndicator

class Option14(base_types._BaseFieldType):

	__slots__ = ["_BrrrInd", "_EvtTp", "_OptnStyle", "_OptnTp", "_XprtnStyle"]
	@property
	def BrrrInd(self):
		return self._BrrrInd

	@BrrrInd.setter
	def BrrrInd(self, value):
		self._BrrrInd = value if value is not None else base_types.UninitialisedField(self, 'BrrrInd', TrueFalseIndicator, False)

	@BrrrInd.deleter
	def BrrrInd(self):
		del self._BrrrInd
		self._BrrrInd = base_types.UninitialisedField(self, 'BrrrInd', TrueFalseIndicator, False)

	@property
	def EvtTp(self):
		return self._EvtTp

	@EvtTp.setter
	def EvtTp(self, value):
		self._EvtTp = value if value is not None else base_types.UninitialisedField(self, 'EvtTp', OptionEvent2, False)

	@EvtTp.deleter
	def EvtTp(self):
		del self._EvtTp
		self._EvtTp = base_types.UninitialisedField(self, 'EvtTp', OptionEvent2, False)

	@property
	def OptnStyle(self):
		return self._OptnStyle

	@OptnStyle.setter
	def OptnStyle(self, value):
		self._OptnStyle = value if value is not None else base_types.UninitialisedField(self, 'OptnStyle', ExoticOptionStyle1Code, False)

	@OptnStyle.deleter
	def OptnStyle(self):
		del self._OptnStyle
		self._OptnStyle = base_types.UninitialisedField(self, 'OptnStyle', ExoticOptionStyle1Code, False)

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if value is not None else base_types.UninitialisedField(self, 'OptnTp', OptionType1Code, False)

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = base_types.UninitialisedField(self, 'OptnTp', OptionType1Code, False)

	@property
	def XprtnStyle(self):
		return self._XprtnStyle

	@XprtnStyle.setter
	def XprtnStyle(self, value):
		self._XprtnStyle = value if value is not None else base_types.UninitialisedField(self, 'XprtnStyle', OptionStyle5Code, True)

	@XprtnStyle.deleter
	def XprtnStyle(self):
		del self._XprtnStyle
		self._XprtnStyle = base_types.UninitialisedField(self, 'XprtnStyle', OptionStyle5Code, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BrrrInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtTp', type=OptionEvent2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnStyle', type=ExoticOptionStyle1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=OptionType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XprtnStyle', type=OptionStyle5Code, min=1, max=4, mutex_group=None, array=True),
	))