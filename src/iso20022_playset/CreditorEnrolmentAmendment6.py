import base_types
import CreditorEnrolment6
import CreditorInvoice5

class CreditorEnrolmentAmendment6(base_types._BaseFieldType):

	__slots__ = ["_ActvtnData", "_CdtrEnrlmnt"]
	@property
	def ActvtnData(self):
		return self._ActvtnData

	@ActvtnData.setter
	def ActvtnData(self, value):
		self._ActvtnData = value if type(value) != auto else self.make_default("ActvtnData")

	@ActvtnData.deleter
	def ActvtnData(self):
		del self._ActvtnData
		self._ActvtnData = None

	@property
	def CdtrEnrlmnt(self):
		return self._CdtrEnrlmnt

	@CdtrEnrlmnt.setter
	def CdtrEnrlmnt(self, value):
		self._CdtrEnrlmnt = value if type(value) != auto else self.make_default("CdtrEnrlmnt")

	@CdtrEnrlmnt.deleter
	def CdtrEnrlmnt(self):
		del self._CdtrEnrlmnt
		self._CdtrEnrlmnt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActvtnData', type=CreditorInvoice5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrEnrlmnt', type=CreditorEnrolment6, min=0, max=1, mutex_group=None, array=False),
	))

