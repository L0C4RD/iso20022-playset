# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification36
from . import Max350Text

class AdditionalInformation15(base_types._BaseFieldType):

	__slots__ = ["_InfTp", "_InfVal"]
	@property
	def InfTp(self):
		return self._InfTp

	@InfTp.setter
	def InfTp(self, value):
		self._InfTp = value if value is not None else base_types.UninitialisedField(self, 'InfTp', GenericIdentification36, False)

	@InfTp.deleter
	def InfTp(self):
		del self._InfTp
		self._InfTp = base_types.UninitialisedField(self, 'InfTp', GenericIdentification36, False)

	@property
	def InfVal(self):
		return self._InfVal

	@InfVal.setter
	def InfVal(self, value):
		self._InfVal = value if value is not None else base_types.UninitialisedField(self, 'InfVal', Max350Text, False)

	@InfVal.deleter
	def InfVal(self):
		del self._InfVal
		self._InfVal = base_types.UninitialisedField(self, 'InfVal', Max350Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InfTp', type=GenericIdentification36, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfVal', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
	))