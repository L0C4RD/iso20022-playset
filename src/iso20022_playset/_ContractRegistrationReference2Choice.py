# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DocumentIdentification35 import DocumentIdentification35
from ._Max35Text import Max35Text

class ContractRegistrationReference2Choice(base_types._BaseFieldType):

	__slots__ = ["_Ctrct", "_RegdCtrctId"]
	@property
	def Ctrct(self):
		return self._Ctrct

	@Ctrct.setter
	def Ctrct(self, value):
		self._Ctrct = value if type(value) != base_types.auto else self.make_default("Ctrct")

	@Ctrct.deleter
	def Ctrct(self):
		del self._Ctrct
		self._Ctrct = None

	@property
	def RegdCtrctId(self):
		return self._RegdCtrctId

	@RegdCtrctId.setter
	def RegdCtrctId(self, value):
		self._RegdCtrctId = value if type(value) != base_types.auto else self.make_default("RegdCtrctId")

	@RegdCtrctId.deleter
	def RegdCtrctId(self):
		del self._RegdCtrctId
		self._RegdCtrctId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ctrct', type=DocumentIdentification35, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RegdCtrctId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))