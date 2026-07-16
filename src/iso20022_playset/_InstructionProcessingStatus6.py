# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max350Text
from . import Max35Text
from . import Status11Code

class InstructionProcessingStatus6(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AttndncCardNb", "_Sts"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max350Text, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max350Text, False)

	@property
	def AttndncCardNb(self):
		return self._AttndncCardNb

	@AttndncCardNb.setter
	def AttndncCardNb(self, value):
		self._AttndncCardNb = value if value is not None else base_types.UninitialisedField(self, 'AttndncCardNb', Max35Text, False)

	@AttndncCardNb.deleter
	def AttndncCardNb(self):
		del self._AttndncCardNb
		self._AttndncCardNb = base_types.UninitialisedField(self, 'AttndncCardNb', Max35Text, False)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', Status11Code, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', Status11Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AttndncCardNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=Status11Code, min=1, max=1, mutex_group=None, array=False),
	))