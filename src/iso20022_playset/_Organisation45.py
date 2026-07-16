# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CommunicationAddress9
from . import GenericIdentification192
from . import LocationCategory4Code
from . import Max140Text
from . import Max70Text

class Organisation45(base_types._BaseFieldType):

	__slots__ = ["_CmonNm", "_Id", "_LctnAndCtct", "_LctnCtgy", "_SchmeData"]
	@property
	def CmonNm(self):
		return self._CmonNm

	@CmonNm.setter
	def CmonNm(self, value):
		self._CmonNm = value if value is not None else base_types.UninitialisedField(self, 'CmonNm', Max70Text, False)

	@CmonNm.deleter
	def CmonNm(self):
		del self._CmonNm
		self._CmonNm = base_types.UninitialisedField(self, 'CmonNm', Max70Text, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', GenericIdentification192, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', GenericIdentification192, False)

	@property
	def LctnAndCtct(self):
		return self._LctnAndCtct

	@LctnAndCtct.setter
	def LctnAndCtct(self, value):
		self._LctnAndCtct = value if value is not None else base_types.UninitialisedField(self, 'LctnAndCtct', CommunicationAddress9, False)

	@LctnAndCtct.deleter
	def LctnAndCtct(self):
		del self._LctnAndCtct
		self._LctnAndCtct = base_types.UninitialisedField(self, 'LctnAndCtct', CommunicationAddress9, False)

	@property
	def LctnCtgy(self):
		return self._LctnCtgy

	@LctnCtgy.setter
	def LctnCtgy(self, value):
		self._LctnCtgy = value if value is not None else base_types.UninitialisedField(self, 'LctnCtgy', LocationCategory4Code, False)

	@LctnCtgy.deleter
	def LctnCtgy(self):
		del self._LctnCtgy
		self._LctnCtgy = base_types.UninitialisedField(self, 'LctnCtgy', LocationCategory4Code, False)

	@property
	def SchmeData(self):
		return self._SchmeData

	@SchmeData.setter
	def SchmeData(self, value):
		self._SchmeData = value if value is not None else base_types.UninitialisedField(self, 'SchmeData', Max140Text, False)

	@SchmeData.deleter
	def SchmeData(self):
		del self._SchmeData
		self._SchmeData = base_types.UninitialisedField(self, 'SchmeData', Max140Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CmonNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=GenericIdentification192, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LctnAndCtct', type=CommunicationAddress9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LctnCtgy', type=LocationCategory4Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SchmeData', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))