# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Exact3UpperCaseAlphaNumericText
from . import GenericIdentification36
from . import Max30Text

class IdentificationFormat3Choice(base_types._BaseFieldType):

	__slots__ = ["_LngId", "_PrtryId", "_ShrtId"]
	@property
	def LngId(self):
		return self._LngId

	@LngId.setter
	def LngId(self, value):
		self._LngId = value if value is not None else base_types.UninitialisedField(self, 'LngId', Max30Text, False)

	@LngId.deleter
	def LngId(self):
		del self._LngId
		self._LngId = base_types.UninitialisedField(self, 'LngId', Max30Text, False)

	@property
	def PrtryId(self):
		return self._PrtryId

	@PrtryId.setter
	def PrtryId(self, value):
		self._PrtryId = value if value is not None else base_types.UninitialisedField(self, 'PrtryId', GenericIdentification36, False)

	@PrtryId.deleter
	def PrtryId(self):
		del self._PrtryId
		self._PrtryId = base_types.UninitialisedField(self, 'PrtryId', GenericIdentification36, False)

	@property
	def ShrtId(self):
		return self._ShrtId

	@ShrtId.setter
	def ShrtId(self, value):
		self._ShrtId = value if value is not None else base_types.UninitialisedField(self, 'ShrtId', Exact3UpperCaseAlphaNumericText, False)

	@ShrtId.deleter
	def ShrtId(self):
		del self._ShrtId
		self._ShrtId = base_types.UninitialisedField(self, 'ShrtId', Exact3UpperCaseAlphaNumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LngId', type=Max30Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtryId', type=GenericIdentification36, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ShrtId', type=Exact3UpperCaseAlphaNumericText, min=0, max=1, mutex_group=1, array=False),
	))