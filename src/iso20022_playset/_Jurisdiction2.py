# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import TrueFalseIndicator

class Jurisdiction2(base_types._BaseFieldType):

	__slots__ = ["_DmstInd", "_DmstQlfctn"]
	@property
	def DmstInd(self):
		return self._DmstInd

	@DmstInd.setter
	def DmstInd(self, value):
		self._DmstInd = value if value is not None else base_types.UninitialisedField(self, 'DmstInd', TrueFalseIndicator, False)

	@DmstInd.deleter
	def DmstInd(self):
		del self._DmstInd
		self._DmstInd = base_types.UninitialisedField(self, 'DmstInd', TrueFalseIndicator, False)

	@property
	def DmstQlfctn(self):
		return self._DmstQlfctn

	@DmstQlfctn.setter
	def DmstQlfctn(self, value):
		self._DmstQlfctn = value if value is not None else base_types.UninitialisedField(self, 'DmstQlfctn', Max35Text, False)

	@DmstQlfctn.deleter
	def DmstQlfctn(self):
		del self._DmstQlfctn
		self._DmstQlfctn = base_types.UninitialisedField(self, 'DmstQlfctn', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DmstInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmstQlfctn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))