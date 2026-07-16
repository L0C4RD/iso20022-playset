# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CreditorEnrolment5
from . import Party53Choice

class OriginalEnrolment3Choice(base_types._BaseFieldType):

	__slots__ = ["_OrgnlCdtrId", "_OrgnlEnrlmntData"]
	@property
	def OrgnlCdtrId(self):
		return self._OrgnlCdtrId

	@OrgnlCdtrId.setter
	def OrgnlCdtrId(self, value):
		self._OrgnlCdtrId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlCdtrId', Party53Choice, False)

	@OrgnlCdtrId.deleter
	def OrgnlCdtrId(self):
		del self._OrgnlCdtrId
		self._OrgnlCdtrId = base_types.UninitialisedField(self, 'OrgnlCdtrId', Party53Choice, False)

	@property
	def OrgnlEnrlmntData(self):
		return self._OrgnlEnrlmntData

	@OrgnlEnrlmntData.setter
	def OrgnlEnrlmntData(self, value):
		self._OrgnlEnrlmntData = value if value is not None else base_types.UninitialisedField(self, 'OrgnlEnrlmntData', CreditorEnrolment5, False)

	@OrgnlEnrlmntData.deleter
	def OrgnlEnrlmntData(self):
		del self._OrgnlEnrlmntData
		self._OrgnlEnrlmntData = base_types.UninitialisedField(self, 'OrgnlEnrlmntData', CreditorEnrolment5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlCdtrId', type=Party53Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OrgnlEnrlmntData', type=CreditorEnrolment5, min=0, max=1, mutex_group=1, array=False),
	))