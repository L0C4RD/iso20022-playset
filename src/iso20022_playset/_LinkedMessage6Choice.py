# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AdditionalReference14 import AdditionalReference14

class LinkedMessage6Choice(base_types._BaseFieldType):

	__slots__ = ["_OthrRef", "_PrvsRef", "_RltdRef"]
	@property
	def OthrRef(self):
		return self._OthrRef

	@OthrRef.setter
	def OthrRef(self, value):
		self._OthrRef = value if type(value) != base_types.auto else self.make_default("OthrRef")

	@OthrRef.deleter
	def OthrRef(self):
		del self._OthrRef
		self._OthrRef = None

	@property
	def PrvsRef(self):
		return self._PrvsRef

	@PrvsRef.setter
	def PrvsRef(self, value):
		self._PrvsRef = value if type(value) != base_types.auto else self.make_default("PrvsRef")

	@PrvsRef.deleter
	def PrvsRef(self):
		del self._PrvsRef
		self._PrvsRef = None

	@property
	def RltdRef(self):
		return self._RltdRef

	@RltdRef.setter
	def RltdRef(self, value):
		self._RltdRef = value if type(value) != base_types.auto else self.make_default("RltdRef")

	@RltdRef.deleter
	def RltdRef(self):
		del self._RltdRef
		self._RltdRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrRef', type=AdditionalReference14, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrvsRef', type=AdditionalReference14, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RltdRef', type=AdditionalReference14, min=0, max=1, mutex_group=1, array=False),
	))