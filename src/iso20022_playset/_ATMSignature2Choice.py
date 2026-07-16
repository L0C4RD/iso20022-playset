# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContentInformationType14
from . import TRRelatedData2

class ATMSignature2Choice(base_types._BaseFieldType):

	__slots__ = ["_DgtlSgntr", "_TRRltdData"]
	@property
	def DgtlSgntr(self):
		return self._DgtlSgntr

	@DgtlSgntr.setter
	def DgtlSgntr(self, value):
		self._DgtlSgntr = value if value is not None else base_types.UninitialisedField(self, 'DgtlSgntr', ContentInformationType14, False)

	@DgtlSgntr.deleter
	def DgtlSgntr(self):
		del self._DgtlSgntr
		self._DgtlSgntr = base_types.UninitialisedField(self, 'DgtlSgntr', ContentInformationType14, False)

	@property
	def TRRltdData(self):
		return self._TRRltdData

	@TRRltdData.setter
	def TRRltdData(self, value):
		self._TRRltdData = value if value is not None else base_types.UninitialisedField(self, 'TRRltdData', TRRelatedData2, False)

	@TRRltdData.deleter
	def TRRltdData(self):
		del self._TRRltdData
		self._TRRltdData = base_types.UninitialisedField(self, 'TRRltdData', TRRelatedData2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntr', type=ContentInformationType14, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TRRltdData', type=TRRelatedData2, min=0, max=1, mutex_group=1, array=False),
	))