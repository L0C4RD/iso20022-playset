# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MessageReference
from . import RejectionReason2

class admi.002.001.01(base_types._BaseFieldType):

	__slots__ = ["_RltdRef", "_Rsn"]
	@property
	def RltdRef(self):
		return self._RltdRef

	@RltdRef.setter
	def RltdRef(self, value):
		self._RltdRef = value if value is not None else base_types.UninitialisedField(self, 'RltdRef', MessageReference, False)

	@RltdRef.deleter
	def RltdRef(self):
		del self._RltdRef
		self._RltdRef = base_types.UninitialisedField(self, 'RltdRef', MessageReference, False)

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', RejectionReason2, False)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', RejectionReason2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RltdRef', type=MessageReference, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=RejectionReason2, min=1, max=1, mutex_group=None, array=False),
	))