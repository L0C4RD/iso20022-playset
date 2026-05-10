from . import base_types
from .AdditionalReference14 import AdditionalReference14
from .RejectionReason69 import RejectionReason69

class SecuritiesMessageRejectionV04(base_types._BaseFieldType):

	__slots__ = ["_RltdRef", "_Rsn"]
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

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != base_types.auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RltdRef', type=AdditionalReference14, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=RejectionReason69, min=1, max=1, mutex_group=None, array=False),
	))

