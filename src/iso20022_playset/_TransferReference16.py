# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalReference10
from . import Max35Text

class TransferReference16(base_types._BaseFieldType):

	__slots__ = ["_ClntRef", "_CtrPtyRef", "_CxlRef", "_RvslRsn", "_TrfConfRef", "_TrfRef"]
	@property
	def ClntRef(self):
		return self._ClntRef

	@ClntRef.setter
	def ClntRef(self, value):
		self._ClntRef = value if value is not None else base_types.UninitialisedField(self, 'ClntRef', AdditionalReference10, False)

	@ClntRef.deleter
	def ClntRef(self):
		del self._ClntRef
		self._ClntRef = base_types.UninitialisedField(self, 'ClntRef', AdditionalReference10, False)

	@property
	def CtrPtyRef(self):
		return self._CtrPtyRef

	@CtrPtyRef.setter
	def CtrPtyRef(self, value):
		self._CtrPtyRef = value if value is not None else base_types.UninitialisedField(self, 'CtrPtyRef', AdditionalReference10, False)

	@CtrPtyRef.deleter
	def CtrPtyRef(self):
		del self._CtrPtyRef
		self._CtrPtyRef = base_types.UninitialisedField(self, 'CtrPtyRef', AdditionalReference10, False)

	@property
	def CxlRef(self):
		return self._CxlRef

	@CxlRef.setter
	def CxlRef(self, value):
		self._CxlRef = value if value is not None else base_types.UninitialisedField(self, 'CxlRef', Max35Text, False)

	@CxlRef.deleter
	def CxlRef(self):
		del self._CxlRef
		self._CxlRef = base_types.UninitialisedField(self, 'CxlRef', Max35Text, False)

	@property
	def RvslRsn(self):
		return self._RvslRsn

	@RvslRsn.setter
	def RvslRsn(self, value):
		self._RvslRsn = value if value is not None else base_types.UninitialisedField(self, 'RvslRsn', Max35Text, False)

	@RvslRsn.deleter
	def RvslRsn(self):
		del self._RvslRsn
		self._RvslRsn = base_types.UninitialisedField(self, 'RvslRsn', Max35Text, False)

	@property
	def TrfConfRef(self):
		return self._TrfConfRef

	@TrfConfRef.setter
	def TrfConfRef(self, value):
		self._TrfConfRef = value if value is not None else base_types.UninitialisedField(self, 'TrfConfRef', Max35Text, False)

	@TrfConfRef.deleter
	def TrfConfRef(self):
		del self._TrfConfRef
		self._TrfConfRef = base_types.UninitialisedField(self, 'TrfConfRef', Max35Text, False)

	@property
	def TrfRef(self):
		return self._TrfRef

	@TrfRef.setter
	def TrfRef(self, value):
		self._TrfRef = value if value is not None else base_types.UninitialisedField(self, 'TrfRef', Max35Text, False)

	@TrfRef.deleter
	def TrfRef(self):
		del self._TrfRef
		self._TrfRef = base_types.UninitialisedField(self, 'TrfRef', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClntRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvslRsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfConfRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))