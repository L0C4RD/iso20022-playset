import base_types
import DateAndType1
import DocumentType1
import Max35Text

class ReferredMandateDocument2(base_types._BaseFieldType):

	__slots__ = ["_Nb", "_CdtrRef", "_RltdDt", "_Tp"]
	@property
	def Nb(self):
		return self._Nb

	@Nb.setter
	def Nb(self, value):
		self._Nb = value if type(value) != auto else self.make_default("Nb")

	@Nb.deleter
	def Nb(self):
		del self._Nb
		self._Nb = None

	@property
	def CdtrRef(self):
		return self._CdtrRef

	@CdtrRef.setter
	def CdtrRef(self, value):
		self._CdtrRef = value if type(value) != auto else self.make_default("CdtrRef")

	@CdtrRef.deleter
	def CdtrRef(self):
		del self._CdtrRef
		self._CdtrRef = None

	@property
	def RltdDt(self):
		return self._RltdDt

	@RltdDt.setter
	def RltdDt(self, value):
		self._RltdDt = value if type(value) != auto else self.make_default("RltdDt")

	@RltdDt.deleter
	def RltdDt(self):
		del self._RltdDt
		self._RltdDt = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Nb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdDt', type=DateAndType1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=DocumentType1, min=0, max=1, mutex_group=None, array=False),
	))

