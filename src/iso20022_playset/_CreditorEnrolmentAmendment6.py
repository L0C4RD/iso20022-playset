# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CreditorEnrolment6
from . import CreditorInvoice5

class CreditorEnrolmentAmendment6(base_types._BaseFieldType):

	__slots__ = ["_ActvtnData", "_CdtrEnrlmnt"]
	@property
	def ActvtnData(self):
		return self._ActvtnData

	@ActvtnData.setter
	def ActvtnData(self, value):
		self._ActvtnData = value if value is not None else base_types.UninitialisedField(self, 'ActvtnData', CreditorInvoice5, False)

	@ActvtnData.deleter
	def ActvtnData(self):
		del self._ActvtnData
		self._ActvtnData = base_types.UninitialisedField(self, 'ActvtnData', CreditorInvoice5, False)

	@property
	def CdtrEnrlmnt(self):
		return self._CdtrEnrlmnt

	@CdtrEnrlmnt.setter
	def CdtrEnrlmnt(self, value):
		self._CdtrEnrlmnt = value if value is not None else base_types.UninitialisedField(self, 'CdtrEnrlmnt', CreditorEnrolment6, False)

	@CdtrEnrlmnt.deleter
	def CdtrEnrlmnt(self):
		del self._CdtrEnrlmnt
		self._CdtrEnrlmnt = base_types.UninitialisedField(self, 'CdtrEnrlmnt', CreditorEnrolment6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActvtnData', type=CreditorInvoice5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrEnrlmnt', type=CreditorEnrolment6, min=0, max=1, mutex_group=None, array=False),
	))