# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateFormat58Choice
from . import Max350Text
from . import PowerOfAttorneyLegalisation1Code

class PowerOfAttorneyRequirements4(base_types._BaseFieldType):

	__slots__ = ["_DocSubmissnDdln", "_LglRqrmnt", "_OthrDcmnttn"]
	@property
	def DocSubmissnDdln(self):
		return self._DocSubmissnDdln

	@DocSubmissnDdln.setter
	def DocSubmissnDdln(self, value):
		self._DocSubmissnDdln = value if value is not None else base_types.UninitialisedField(self, 'DocSubmissnDdln', DateFormat58Choice, False)

	@DocSubmissnDdln.deleter
	def DocSubmissnDdln(self):
		del self._DocSubmissnDdln
		self._DocSubmissnDdln = base_types.UninitialisedField(self, 'DocSubmissnDdln', DateFormat58Choice, False)

	@property
	def LglRqrmnt(self):
		return self._LglRqrmnt

	@LglRqrmnt.setter
	def LglRqrmnt(self, value):
		self._LglRqrmnt = value if value is not None else base_types.UninitialisedField(self, 'LglRqrmnt', PowerOfAttorneyLegalisation1Code, True)

	@LglRqrmnt.deleter
	def LglRqrmnt(self):
		del self._LglRqrmnt
		self._LglRqrmnt = base_types.UninitialisedField(self, 'LglRqrmnt', PowerOfAttorneyLegalisation1Code, True)

	@property
	def OthrDcmnttn(self):
		return self._OthrDcmnttn

	@OthrDcmnttn.setter
	def OthrDcmnttn(self, value):
		self._OthrDcmnttn = value if value is not None else base_types.UninitialisedField(self, 'OthrDcmnttn', Max350Text, False)

	@OthrDcmnttn.deleter
	def OthrDcmnttn(self):
		del self._OthrDcmnttn
		self._OthrDcmnttn = base_types.UninitialisedField(self, 'OthrDcmnttn', Max350Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DocSubmissnDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglRqrmnt', type=PowerOfAttorneyLegalisation1Code, min=0, max=4, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrDcmnttn', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))