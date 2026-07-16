# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Addition2
from . import Deletion2
from . import Max350Text
from . import Max35Text
from . import Number
from . import Replacement2

class ComparisonResult2(base_types._BaseFieldType):

	__slots__ = ["_Addtn", "_Deltn", "_ElmtNm", "_ElmtPth", "_ElmtSeqNb", "_Rplcmnt"]
	@property
	def Addtn(self):
		return self._Addtn

	@Addtn.setter
	def Addtn(self, value):
		self._Addtn = value if value is not None else base_types.UninitialisedField(self, 'Addtn', Addition2, False)

	@Addtn.deleter
	def Addtn(self):
		del self._Addtn
		self._Addtn = base_types.UninitialisedField(self, 'Addtn', Addition2, False)

	@property
	def Deltn(self):
		return self._Deltn

	@Deltn.setter
	def Deltn(self, value):
		self._Deltn = value if value is not None else base_types.UninitialisedField(self, 'Deltn', Deletion2, False)

	@Deltn.deleter
	def Deltn(self):
		del self._Deltn
		self._Deltn = base_types.UninitialisedField(self, 'Deltn', Deletion2, False)

	@property
	def ElmtNm(self):
		return self._ElmtNm

	@ElmtNm.setter
	def ElmtNm(self, value):
		self._ElmtNm = value if value is not None else base_types.UninitialisedField(self, 'ElmtNm', Max35Text, False)

	@ElmtNm.deleter
	def ElmtNm(self):
		del self._ElmtNm
		self._ElmtNm = base_types.UninitialisedField(self, 'ElmtNm', Max35Text, False)

	@property
	def ElmtPth(self):
		return self._ElmtPth

	@ElmtPth.setter
	def ElmtPth(self, value):
		self._ElmtPth = value if value is not None else base_types.UninitialisedField(self, 'ElmtPth', Max350Text, False)

	@ElmtPth.deleter
	def ElmtPth(self):
		del self._ElmtPth
		self._ElmtPth = base_types.UninitialisedField(self, 'ElmtPth', Max350Text, False)

	@property
	def ElmtSeqNb(self):
		return self._ElmtSeqNb

	@ElmtSeqNb.setter
	def ElmtSeqNb(self, value):
		self._ElmtSeqNb = value if value is not None else base_types.UninitialisedField(self, 'ElmtSeqNb', Number, False)

	@ElmtSeqNb.deleter
	def ElmtSeqNb(self):
		del self._ElmtSeqNb
		self._ElmtSeqNb = base_types.UninitialisedField(self, 'ElmtSeqNb', Number, False)

	@property
	def Rplcmnt(self):
		return self._Rplcmnt

	@Rplcmnt.setter
	def Rplcmnt(self, value):
		self._Rplcmnt = value if value is not None else base_types.UninitialisedField(self, 'Rplcmnt', Replacement2, False)

	@Rplcmnt.deleter
	def Rplcmnt(self):
		del self._Rplcmnt
		self._Rplcmnt = base_types.UninitialisedField(self, 'Rplcmnt', Replacement2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Addtn', type=Addition2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Deltn', type=Deletion2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ElmtNm', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElmtPth', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElmtSeqNb', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rplcmnt', type=Replacement2, min=0, max=1, mutex_group=1, array=False),
	))