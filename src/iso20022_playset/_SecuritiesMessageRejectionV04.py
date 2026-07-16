# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalReference14
from . import RejectionReason69

class SecuritiesMessageRejectionV04(base_types._BaseFieldType):

	__slots__ = ["_RltdRef", "_Rsn"]
	@property
	def RltdRef(self):
		return self._RltdRef

	@RltdRef.setter
	def RltdRef(self, value):
		self._RltdRef = value if value is not None else base_types.UninitialisedField(self, 'RltdRef', AdditionalReference14, False)

	@RltdRef.deleter
	def RltdRef(self):
		del self._RltdRef
		self._RltdRef = base_types.UninitialisedField(self, 'RltdRef', AdditionalReference14, False)

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', RejectionReason69, False)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', RejectionReason69, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RltdRef', type=AdditionalReference14, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=RejectionReason69, min=1, max=1, mutex_group=None, array=False),
	))