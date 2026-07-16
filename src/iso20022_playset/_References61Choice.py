# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalReference8

class References61Choice(base_types._BaseFieldType):

	__slots__ = ["_OthrRef", "_RltdRef"]
	@property
	def OthrRef(self):
		return self._OthrRef

	@OthrRef.setter
	def OthrRef(self, value):
		self._OthrRef = value if value is not None else base_types.UninitialisedField(self, 'OthrRef', AdditionalReference8, False)

	@OthrRef.deleter
	def OthrRef(self):
		del self._OthrRef
		self._OthrRef = base_types.UninitialisedField(self, 'OthrRef', AdditionalReference8, False)

	@property
	def RltdRef(self):
		return self._RltdRef

	@RltdRef.setter
	def RltdRef(self, value):
		self._RltdRef = value if value is not None else base_types.UninitialisedField(self, 'RltdRef', AdditionalReference8, False)

	@RltdRef.deleter
	def RltdRef(self):
		del self._RltdRef
		self._RltdRef = base_types.UninitialisedField(self, 'RltdRef', AdditionalReference8, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrRef', type=AdditionalReference8, min=1, max=2, mutex_group=1, array=False),
		base_types.FieldEntry(name='RltdRef', type=AdditionalReference8, min=1, max=2, mutex_group=1, array=False),
	))