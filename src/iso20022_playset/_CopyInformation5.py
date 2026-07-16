# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AnyBICDec2014Identifier
from . import YesNoIndicator

class CopyInformation5(base_types._BaseFieldType):

	__slots__ = ["_CpyInd", "_OrgnlRcvr"]
	@property
	def CpyInd(self):
		return self._CpyInd

	@CpyInd.setter
	def CpyInd(self, value):
		self._CpyInd = value if value is not None else base_types.UninitialisedField(self, 'CpyInd', YesNoIndicator, False)

	@CpyInd.deleter
	def CpyInd(self):
		del self._CpyInd
		self._CpyInd = base_types.UninitialisedField(self, 'CpyInd', YesNoIndicator, False)

	@property
	def OrgnlRcvr(self):
		return self._OrgnlRcvr

	@OrgnlRcvr.setter
	def OrgnlRcvr(self, value):
		self._OrgnlRcvr = value if value is not None else base_types.UninitialisedField(self, 'OrgnlRcvr', AnyBICDec2014Identifier, False)

	@OrgnlRcvr.deleter
	def OrgnlRcvr(self):
		del self._OrgnlRcvr
		self._OrgnlRcvr = base_types.UninitialisedField(self, 'OrgnlRcvr', AnyBICDec2014Identifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CpyInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlRcvr', type=AnyBICDec2014Identifier, min=0, max=1, mutex_group=None, array=False),
	))