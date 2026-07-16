# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NoReasonCode
from . import ReportItemStatus1

class ReportItemStatus1Choice(base_types._BaseFieldType):

	__slots__ = ["_Accptd", "_AccptdWthXcptn", "_Rjctd"]
	@property
	def Accptd(self):
		return self._Accptd

	@Accptd.setter
	def Accptd(self, value):
		self._Accptd = value if value is not None else base_types.UninitialisedField(self, 'Accptd', NoReasonCode, False)

	@Accptd.deleter
	def Accptd(self):
		del self._Accptd
		self._Accptd = base_types.UninitialisedField(self, 'Accptd', NoReasonCode, False)

	@property
	def AccptdWthXcptn(self):
		return self._AccptdWthXcptn

	@AccptdWthXcptn.setter
	def AccptdWthXcptn(self, value):
		self._AccptdWthXcptn = value if value is not None else base_types.UninitialisedField(self, 'AccptdWthXcptn', ReportItemStatus1, True)

	@AccptdWthXcptn.deleter
	def AccptdWthXcptn(self):
		del self._AccptdWthXcptn
		self._AccptdWthXcptn = base_types.UninitialisedField(self, 'AccptdWthXcptn', ReportItemStatus1, True)

	@property
	def Rjctd(self):
		return self._Rjctd

	@Rjctd.setter
	def Rjctd(self, value):
		self._Rjctd = value if value is not None else base_types.UninitialisedField(self, 'Rjctd', ReportItemStatus1, False)

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = base_types.UninitialisedField(self, 'Rjctd', ReportItemStatus1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Accptd', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AccptdWthXcptn', type=ReportItemStatus1, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='Rjctd', type=ReportItemStatus1, min=0, max=1, mutex_group=1, array=False),
	))