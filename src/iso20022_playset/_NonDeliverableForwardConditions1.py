# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NDFOpeningFixing1Choice
from . import YesNoIndicator

class NonDeliverableForwardConditions1(base_types._BaseFieldType):

	__slots__ = ["_OpngFxgConds", "_OpngInd"]
	@property
	def OpngFxgConds(self):
		return self._OpngFxgConds

	@OpngFxgConds.setter
	def OpngFxgConds(self, value):
		self._OpngFxgConds = value if value is not None else base_types.UninitialisedField(self, 'OpngFxgConds', NDFOpeningFixing1Choice, False)

	@OpngFxgConds.deleter
	def OpngFxgConds(self):
		del self._OpngFxgConds
		self._OpngFxgConds = base_types.UninitialisedField(self, 'OpngFxgConds', NDFOpeningFixing1Choice, False)

	@property
	def OpngInd(self):
		return self._OpngInd

	@OpngInd.setter
	def OpngInd(self, value):
		self._OpngInd = value if value is not None else base_types.UninitialisedField(self, 'OpngInd', YesNoIndicator, False)

	@OpngInd.deleter
	def OpngInd(self):
		del self._OpngInd
		self._OpngInd = base_types.UninitialisedField(self, 'OpngInd', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OpngFxgConds', type=NDFOpeningFixing1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))