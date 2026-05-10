import base_types
import SaleToPOISessionManagementRequestV07

class CASP_005_001_07():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SaleToPOISsnMgmtReq"]
		@property
		def SaleToPOISsnMgmtReq(self):
			return self._SaleToPOISsnMgmtReq

		@SaleToPOISsnMgmtReq.setter
		def SaleToPOISsnMgmtReq(self, value):
			self._SaleToPOISsnMgmtReq = value if type(value) != auto else self.make_default("SaleToPOISsnMgmtReq")

		@SaleToPOISsnMgmtReq.deleter
		def SaleToPOISsnMgmtReq(self):
			del self._SaleToPOISsnMgmtReq
			self._SaleToPOISsnMgmtReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOISsnMgmtReq', type=SaleToPOISessionManagementRequestV07, min=1, max=1, mutex_group=None, array=False),
		))

