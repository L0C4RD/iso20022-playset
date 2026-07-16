# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CreditorEnrolment5
from . import CreditorInvoice6
from . import EnrolmentHeader3
from . import SupplementaryData1

class RequestToPayCreditorEnrolmentRequestV02(base_types._BaseFieldType):

	__slots__ = ["_ActvtnData", "_CdtrEnrlmnt", "_Hdr", "_SplmtryData"]
	@property
	def ActvtnData(self):
		return self._ActvtnData

	@ActvtnData.setter
	def ActvtnData(self, value):
		self._ActvtnData = value if value is not None else base_types.UninitialisedField(self, 'ActvtnData', CreditorInvoice6, False)

	@ActvtnData.deleter
	def ActvtnData(self):
		del self._ActvtnData
		self._ActvtnData = base_types.UninitialisedField(self, 'ActvtnData', CreditorInvoice6, False)

	@property
	def CdtrEnrlmnt(self):
		return self._CdtrEnrlmnt

	@CdtrEnrlmnt.setter
	def CdtrEnrlmnt(self, value):
		self._CdtrEnrlmnt = value if value is not None else base_types.UninitialisedField(self, 'CdtrEnrlmnt', CreditorEnrolment5, True)

	@CdtrEnrlmnt.deleter
	def CdtrEnrlmnt(self):
		del self._CdtrEnrlmnt
		self._CdtrEnrlmnt = base_types.UninitialisedField(self, 'CdtrEnrlmnt', CreditorEnrolment5, True)

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if value is not None else base_types.UninitialisedField(self, 'Hdr', EnrolmentHeader3, False)

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = base_types.UninitialisedField(self, 'Hdr', EnrolmentHeader3, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActvtnData', type=CreditorInvoice6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrEnrlmnt', type=CreditorEnrolment5, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Hdr', type=EnrolmentHeader3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))