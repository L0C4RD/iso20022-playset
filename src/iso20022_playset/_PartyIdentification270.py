# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyAdditionalIdentification2Choice
from . import PartyIdentification246Choice

class PartyIdentification270(base_types._BaseFieldType):

	__slots__ = ["_AddtlIdInf", "_Id"]
	@property
	def AddtlIdInf(self):
		return self._AddtlIdInf

	@AddtlIdInf.setter
	def AddtlIdInf(self, value):
		self._AddtlIdInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlIdInf', PartyAdditionalIdentification2Choice, False)

	@AddtlIdInf.deleter
	def AddtlIdInf(self):
		del self._AddtlIdInf
		self._AddtlIdInf = base_types.UninitialisedField(self, 'AddtlIdInf', PartyAdditionalIdentification2Choice, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', PartyIdentification246Choice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', PartyIdentification246Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlIdInf', type=PartyAdditionalIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification246Choice, min=1, max=1, mutex_group=None, array=False),
	))