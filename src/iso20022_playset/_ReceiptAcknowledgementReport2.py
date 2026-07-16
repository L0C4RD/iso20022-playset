# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MessageReference1
from . import RequestHandling2

class ReceiptAcknowledgementReport2(base_types._BaseFieldType):

	__slots__ = ["_ReqHdlg", "_RltdRef"]
	@property
	def ReqHdlg(self):
		return self._ReqHdlg

	@ReqHdlg.setter
	def ReqHdlg(self, value):
		self._ReqHdlg = value if value is not None else base_types.UninitialisedField(self, 'ReqHdlg', RequestHandling2, False)

	@ReqHdlg.deleter
	def ReqHdlg(self):
		del self._ReqHdlg
		self._ReqHdlg = base_types.UninitialisedField(self, 'ReqHdlg', RequestHandling2, False)

	@property
	def RltdRef(self):
		return self._RltdRef

	@RltdRef.setter
	def RltdRef(self, value):
		self._RltdRef = value if value is not None else base_types.UninitialisedField(self, 'RltdRef', MessageReference1, False)

	@RltdRef.deleter
	def RltdRef(self):
		del self._RltdRef
		self._RltdRef = base_types.UninitialisedField(self, 'RltdRef', MessageReference1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ReqHdlg', type=RequestHandling2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdRef', type=MessageReference1, min=1, max=1, mutex_group=None, array=False),
	))