import base_types
import RequestHandling2
import MessageReference1

class ReceiptAcknowledgementReport2(base_types._BaseFieldType):

	__slots__ = ["_RltdRef", "_ReqHdlg"]
	@property
	def RltdRef(self):
		return self._RltdRef

	@RltdRef.setter
	def RltdRef(self, value):
		self._RltdRef = value if type(value) != auto else self.make_default("RltdRef")

	@RltdRef.deleter
	def RltdRef(self):
		del self._RltdRef
		self._RltdRef = None

	@property
	def ReqHdlg(self):
		return self._ReqHdlg

	@ReqHdlg.setter
	def ReqHdlg(self, value):
		self._ReqHdlg = value if type(value) != auto else self.make_default("ReqHdlg")

	@ReqHdlg.deleter
	def ReqHdlg(self):
		del self._ReqHdlg
		self._ReqHdlg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RltdRef', type=MessageReference1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqHdlg', type=RequestHandling2, min=1, max=1, mutex_group=None, array=False),
	))

